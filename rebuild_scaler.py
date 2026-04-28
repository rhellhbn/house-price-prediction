import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('housing.csv')
df = pd.get_dummies(df, columns=['ocean_proximity'])
df.dropna(inplace=True)

X = df.drop('median_house_value', axis=1)
scaler = MinMaxScaler()
scaler.fit(X)

pickle.dump(scaler, open('scaler_new.pkl', 'wb'))
print("Kolom:", list(X.columns))
print("Jumlah kolom:", len(X.columns))