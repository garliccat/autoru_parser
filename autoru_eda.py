import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

pd.options.display.width = 1000
pd.options.display.max_columns = 100
pd.options.display.max_colwidth = 200

df = pd.read_csv('autoru_cleaned.csv', sep=';')

print(df.head())

### cut high prices
df = df[df['price'] < df['price'].quantile(0.95)]

### gas type vs price plot
gas_types = df['gas_type'].value_counts().index[:2]
df_gas = df[df['gas_type'].isin(gas_types)]
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data=df_gas, 
    x='price', 
    hue='gas_type', 
    bins=50,
    multiple='dodge',
    # kind='hist',
    ax=ax,
    )
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price vs gas type distribution')

plt.show()


### age vs price plot
df_age = df[['year', 'price']].groupby(by='year').agg({'price': ['mean', 'count']})
print(df_age.head())
sns.scatterplot(data=df_age.droplevel(0, axis=1), 
    x=df_age.index, 
    y='mean',
    size='count',
    sizes=(20, 200)
    )

plt.show()
