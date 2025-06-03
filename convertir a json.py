import pandas as pd

# Cargar archivos Excel
df_2022 = pd.read_excel('2022.xlsx')
df_2023 = pd.read_excel('2023.xlsx')

# Guardar como JSON (MongoDB acepta formato de líneas separadas por documento)
df_2022.to_json('2022.json', orient='records', lines=True)
df_2023.to_json('2023.json', orient='records', lines=True)
