import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

# Mean impact force of frog I
np.mean(df.loc[df['ID']=='I', 'impf'])
