# 🏠 House Price Prediction - Artificial Neural Network (ANN)

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3.3-black?style=for-the-badge&logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13.0-orange?style=for-the-badge&logo=tensorflow)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.0-blue?style=for-the-badge&logo=scikitlearn)

Aplikasi web untuk memprediksi harga rumah di California menggunakan model **Deep Learning (ANN)**. Proyek ini mengintegrasikan model yang dilatih menggunakan TensorFlow/Keras ke dalam antarmuka web interaktif berbasis Flask.

## 📁 Struktur Folder
```text
house_price_app/
├── venv/               # Virtual Environment
├── templates/          # Folder file HTML
│   └── index.html      # Tampilan Utama (UI)
├── app.py              # Backend Flask (Route & Model Loader)
├── model_ann.h5        # Model ANN yang sudah dilatih (Trained Model)
├── scaler.pkl          # Pre-trained Scaler (MinMaxScaler)
├── requirements.txt    # Daftar library pendukung
└── README.md           # Dokumentasi proyek
