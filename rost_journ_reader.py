import pandas as pd
import openpyxl
import numpy as np
import re

def xlsx_edit(file):
    df = pd.read_excel(file)

    df = df.loc[:, ['Время', 'Т обр']]

    df['Время'] = df['Время'].apply(lambda x: str(x))
    df['Т обр'] = df['Т обр'].apply(lambda x: str(x))

    df['Время'] = df['Время'].replace('nan', '')
    df['Т обр'] = df['Т обр'].replace('nan', '')

    df['Время'] = df['Время'].apply(lambda x: re.sub(r'\d\d:\d\d:\d\d', '', x))

    curr_date = ''
    df = df.loc[(df['Т обр'] != '') & (df['Т обр'].str.startswith('B'))]
    return df

print(xlsx_edit('sample.xlsx'))