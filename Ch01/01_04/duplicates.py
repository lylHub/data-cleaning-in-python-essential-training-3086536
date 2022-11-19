# %%
import pandas as pd


# %%
df = pd.read_csv('cart.csv', parse_dates=['date'])
df
# %%
df.duplicated()

# %%
df.duplicated(['date', 'name'])

# %%
df.duplicated(['date', 'name']).value_counts()
# %%
