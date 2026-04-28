from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import h5py
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

def build_model():
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(13,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1, activation='linear'),
    ])
    return model

model = build_model()

with h5py.File('model_ann.h5', 'r') as f:
    weight_names = [n.decode('utf8') if isinstance(n, bytes) else n
                    for n in f['model_weights'].attrs['layer_names']]
    for layer in model.layers:
        if layer.name in weight_names:
            g = f['model_weights'][layer.name]
            wnames = [n.decode('utf8') if isinstance(n, bytes) else n
                      for n in g.attrs['weight_names']]
            try:
                layer.set_weights([g[wn][()] for wn in wnames])
            except:
                pass  # skip jika shape tidak cocok

scaler = pickle.load(open('scaler_new.pkl', 'rb'))

def encode_ocean(val):
    # Urutan: <1H OCEAN, INLAND, ISLAND, NEAR BAY, NEAR OCEAN
    mapping = {
        1: [1, 0, 0, 0, 0],  # <1H Ocean
        2: [0, 1, 0, 0, 0],  # Inland
        4: [0, 0, 1, 0, 0],  # Island
        0: [0, 0, 0, 1, 0],  # Near Bay
        3: [0, 0, 0, 0, 1],  # Near Ocean
    }
    return mapping.get(int(val), [1, 0, 0, 0, 0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()
        ocean_encoded = encode_ocean(data['oceanproximity'])

        # 8 numerik + 5 ocean = 13 total
        features = np.array([[
            float(data['longitude']),
            float(data['latitude']),
            float(data['houseage']),
            float(data['houserooms']),
            float(data['totlabedrooms']),
            float(data['population']),
            float(data['households']),
            float(data['medianincome']),
        ] + ocean_encoded])

        features_scaled = scaler.transform(features)
        price = model.predict(features_scaled)[0][0]
        return jsonify({'success': True, 'price': round(float(price), 2)})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)