import pandas as pd
import openpyxl
import numpy as np

file = "sample.xlsx"
df = pd.read_excel(file)

df = df.loc[:, ['Время', 'Т обр']]

df['Время'] = df['Время'].apply(lambda x: str(x))
df['Т обр'] = df['Т обр'].apply(lambda x: str(x))

df['Время'] = df['Время'].replace('nan', '')
df['Т обр'] = df['Т обр'].replace('nan', '')

df['Время'] = df['Время'].str.replace(r'[\d\d:\d\d:\d\d]', '')

print(df.head(50))