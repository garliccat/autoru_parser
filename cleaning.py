import pandas as pd
import re

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

df = pd.read_csv('autoru.csv', header=None, sep=';')
print('Shape before dropping duplicates: {}',format(df.shape))
df = df.drop(df.columns[0], axis=1).drop_duplicates().dropna()
df.columns = ['date', 'title', 'brand', 'model', 'engine', 'gear', 'drive', 'color', 'year', 'mileage', 'price']
print('Shape after dropping the duplicates: {}'.format(df.shape))

# cleaning the price column
df['price'] = df['price'].str.replace(r'[\s₽]', '', regex=True)
df['price'] = pd.to_numeric(df['price'])

# cleaning the mileage column
df['mileage'] = df['mileage'].str.replace('[^0-9]', '', regex=True)
df['mileage'] = pd.to_numeric(df['mileage'])

# fetching engine volume
df['engine_vol'] = df['engine'].apply(lambda x: re.split(r'\sл', x)[0])
df['engine_vol'] = pd.to_numeric(df['engine_vol'])

# fetching hps
df['hps'] = df['engine'].apply(lambda x: re.split(r'\s', x)[3])
df['hps'] = pd.to_numeric(df['hps'])

# fetching fuel
df['fuel'] = df['engine'].apply(lambda x: re.split(r'\s', x)[-1].lower())

df = df.drop('engine', axis=1)

# making date to date
df['date'] = pd.to_datetime(df['date'])

print(df.head())
print(df.info())
print(df.shape)

df.to_csv('dataset.csv', sep=';', index=False, encoding='utf8')
