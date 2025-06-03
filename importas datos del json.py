from pymongo import MongoClient
import json


# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["base_datos_excel"]
coleccion_2022 = db["datos2022"]

# Leer y cargar JSON
with open("2022.json", "r", encoding="utf-8") as f:# cambio luego al 2023 
    datos = [json.loads(line) for line in f]

coleccion_2022.insert_many(datos)
print("Datos 2022 importados con éxito")
