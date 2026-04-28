# House Price Prediction - ANN
Aplikasi prediksi harga rumah California menggunakan Artificial Neural Network + Flask.

---

## Struktur Folder

```
house_price_app/
├── app.py
├── requirements.txt
├── model_ann.h5       ← copy dari zip asli
├── scaler.pkl         ← copy dari zip asli
└── templates/
    └── index.html
```

---

## Tahapan Menjalankan

### 1. Siapkan File Model
Extract zip yang kamu punya, lalu copy 2 file ini ke folder `house_price_app/`:
- `model_ann.h5`
- `scaler.pkl`

### 2. Buat Virtual Environment
```bash
python -m venv venv
```

Aktifkan virtual environment:
- Windows:  `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
python app.py
```

### 5. Buka di Browser
Buka: http://127.0.0.1:5000

---

## Contoh Input Data

| Field            | Contoh Nilai |
|------------------|-------------|
| Longitude        | -122.23     |
| Latitude         | 37.88       |
| Ocean Proximity  | Near Bay    |
| Usia Rumah       | 41          |
| Total Kamar      | 880         |
| Total Kamar Tidur| 129         |
| Populasi         | 322         |
| Rumah Tangga     | 126         |
| Median Income    | 8.33        |
