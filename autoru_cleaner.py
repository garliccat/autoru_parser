import pandas as pd
import numpy as np
import datetime
import re

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 300)
pd.set_option('display.width', 1000)


df = pd.read_csv('autoru.csv', sep=';')
df.columns = ['id', 'date', 'title', 'brand', 'model', 'engine', 'gear', 'drive', 'color', 'year', 'mileage', 'price']
df = df.drop(['id', 'date'], axis=1)

df = df.drop(17066)
df['eng_vol'] = pd.to_numeric(df['engine'].apply(lambda x: x.split()[0]))
df['hps'] = pd.to_numeric(df['engine'].apply(lambda x: x.split()[3]))
df['gas_type'] = df['engine'].apply(lambda x: x.split()[-1])
df = df.drop('engine', axis=1)
df['mileage'] = pd.to_numeric(df['mileage'].apply(lambda x: re.sub(r'[\D]', '', x)), downcast='integer')
df['price'] = pd.to_numeric(df['price'].apply(lambda x: re.sub(r'[\D]', '', str(x))), downcast='integer').astype('Int64')
df = df[~df['price'].isna()]

# df = pd.read_csv('cleaned.csv', sep=';')

print(df.head(10))
print(df.info())
print(df.describe())
df.to_csv('cleaned.csv', sep=';', index=False)