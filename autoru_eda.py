import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

pd.options.display.width = 1000
pd.options.display.max_columns = 100
pd.options.display.max_colwidth = 200

source = pd.read_csv('autoru_cleaned.csv', sep=';')

### cut high prices
df = source[source['price'] < source['price'].quantile(0.95)]

### colors popularity before 1990
colors = df[['year', 'color', 'hps']].groupby(['year', 'color'], as_index=False).count()
colors = colors[colors['year'] <= 1990]
colors = colors.pivot_table(values='hps', 
    index='color', 
    columns='year', 
    aggfunc='sum', 
    fill_value=0)
plt.figure(figsize=(10, 5))
sns.heatmap(colors,
    robust=True,
    cbar_kws={'label': 'Count'},
    cmap='viridis'
    )
plt.xticks(rotation=90)
plt.title('Car color popularity up to 1990')
plt.xlabel('Year')
plt.ylabel('Color')
plt.tight_layout()
plt.savefig('plots/colors_year_1990.jpg')
# plt.show()
plt.close()

### color popularity from 1990 up to today
colors = df[['year', 'color', 'hps']].groupby(['year', 'color'], as_index=False).count()
colors = colors[colors['year'] > 1990]
colors = colors.pivot_table(values='hps', 
    index='color', 
    columns='year', 
    aggfunc='sum', 
    fill_value=0)
plt.figure(figsize=(10, 5))
sns.heatmap(colors,
    robust=True,
    cbar_kws={'label': 'Count'},
    cmap='viridis'
    )
plt.xticks(rotation=90)
plt.title('Car color popularity starting 1990')
plt.xlabel('Year')
plt.ylabel('Color')
plt.tight_layout()
plt.savefig('plots/colors_after_1990.jpg')
# plt.show()
plt.close()


### gas type vs price plot
# gas_types = df['gas_type'].value_counts().index[:2]
# df_gas = df[df['gas_type'].isin(gas_types)]
# fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x=df['gas_type'],
    y=df['price'])
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price vs gas type distribution')
plt.savefig('plots/gas_price.jpg')
# plt.show()
plt.close()


### age vs price plot
df_age = df[['year', 'price']].groupby(by='year').agg({'price': ['mean', 'count']})
print(df_age.head())
sns.scatterplot(data=df_age.droplevel(0, axis=1), 
    x=df_age.index, 
    y='mean',
    size='count',
    sizes=(20, 200)
    )
plt.ylabel('Mean price')
plt.xlabel('Production year')
plt.title('Mean price vs Production year', fontsize=20)

# plt.show()
plt.close()
