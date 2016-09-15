import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df.loc[df['adhesive strength (Pa)']<-2000, ["impact time (ms)"]]

df.loc[df['ID']=='II', ['impact force (mN)', 'adhesive force (mN)']]

df.loc[(df['ID']=='III') | (df['ID']=='IV') , ['time frog pulls on target (ms)', 'adhesive force (mN)']]




#a
np.mean(df.loc[df['ID']=='II', ['impact force (mN)']])

frogs=["I","II",'III','IV']
impact=[]
for each in frogs:
    impact.append([each,np.mean(df.loc[df['ID']==each, ['impact force (mN)']])])

np.array(impact)








# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

#a
df_std_impf = grouped.apply(np.std)

#b
def coeff_of_var(data):
    """variance divided by mean"""
    return np.std(data)/np.mean(data)

#c
df_impf = df.loc[:, ['ID', 'impact force (mN)','adhesive force (mN)']]
grouped = df_impf.groupby('ID')
grouped.agg([coeff_of_var])

#d
grouped.agg([np.mean,np.median,np.std,coeff_of_var])
