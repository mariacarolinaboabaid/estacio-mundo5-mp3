import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')
data_copy = data.copy()
# Substitui os valores nulos em 'Calories' por zero
data_copy['Calories'] = data_copy['Calories'].fillna(0)

# Substitui os valores nulos em 'Date' por '1900/01/01'
data_copy['Date'] = data_copy['Date'].fillna('1900/01/01')

# Transforma os dados de 'Date' em datetime
data_copy['Date'] = data_copy['Date'].str.replace("'", "", regex=False)
data_copy['Date'] = data_copy['Date'].str.replace('20201226', '2020/12/26')
data_copy['Date'] = data_copy['Date'].replace('1900/01/01', np.nan)
data_copy['Date'] = pd.to_datetime(data_copy['Date'], format='%Y/%m/%d', errors='coerce')

# Remove registros contendo valores nulos
data_copy = data_copy.dropna()

print(data_copy)