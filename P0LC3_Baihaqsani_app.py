from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Mencoba load data CSV dan mengkonversi nya ke dictionary saat API pertama kali di jalankan
try:
  df = pd.read_csv('P0LC3__data_clean.csv')
  # Orient="records" akan mengubah tabel menjadi list berisi dictionary
  data_clean = df.to_dict(orient="records")
except FileNotFoundError:
  data_clean = []


@app.get("/")
def home():
  return {"message" : "API data clean"}

# Menampilkan seluruh entry data
@app.get("/data")
def mendapatkan_semua_data():
  return{
      "total_data" : len(data_clean),
      "data": data_clean
  }