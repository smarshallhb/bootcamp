import numpy as np

# Pandas, conventionally imported as pd
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)





# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Müller': 14,
           'Fontaine': 13,
           'Pelé': 12,
           'Koscis': 11,
           'Klinsmann': 11}

# Create a Series from the dictionary
s_goals = pd.Series(wc_dict)

# Dictionary of nations
nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Müller': 'Germany',
               'Fontaine': 'France',
               'Pelé': 'Brazil',
               'Koscis': 'Hungary',
               'Klinsmann': 'Germany'}

# Series with nations
s_nation = pd.Series(nation_dict)

df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})
