import numpy as np

# Pandas, conventionally imported as pd
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#4.1a
grant_1973=pd.read_csv('data/grant_1973.csv', comment='#', header=0)
grant_1975=pd.read_csv('data/grant_1975.csv', comment='#', header=0)
grant_1987=pd.read_csv('data/grant_1987.csv', comment='#', header=0)
grant_1991=pd.read_csv('data/grant_1991.csv', comment='#', header=0)
grant_2012=pd.read_csv('data/grant_2012.csv', comment='#', header=0)
grant_complete=pd.read_csv('data/grant_complete.csv', comment='#', header=0)

#b1
grant_1973=grant_1973.rename(columns={'yearband':'year'})
grant_1973["year"]=1973

#2
grant_1975["year"]=1975
grant_1987["year"]=1987
grant_1991["year"]=1991
grant_2012["year"]=2012

#3
def fix_columns(grant):
    grant=grant.rename(columns={'beak depth':'beak depth (mm)'})
    grant=grant.rename(columns={'beak length':'beak length (mm)'})
    grant=grant.rename(columns={'Beak depth, mm':'beak depth (mm)'})
    grant=grant.rename(columns={'Beak length, mm':'beak length (mm)'})
    grant=grant.rename(columns={'bdepth':'beak depth (mm)'})
    grant=grant.rename(columns={'blength':'beak length (mm)'})
    return grant


grant_1973=fix_columns(grant_1973)

grant_1975=fix_columns(grant_1975)

grant_1987=fix_columns(grant_1987)

grant_1991=fix_columns(grant_1991)

grant_2012=fix_columns(grant_2012)

#4
grant_all = pd.concat((grant_1973,grant_1975,grant_1987,grant_1991,grant_2012),ignore_index=True)

#5
grant_all.to_csv('grant_all.csv', index=True)

#c
grant_all=grant_all.drop_duplicates(["year","band"])

#d

def ecdf(data):
    """calculate ecdf"""
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / float(len(x))
    return x, y

x_1987f, y_1987f= ecdf(grant_1987.loc[grant_1987["species"]=="fortis" ,["beak depth (mm)"]])
x_1987s, y_1987s= ecdf(grant_1987.loc[grant_1987["species"]=="scandens" ,["beak depth (mm)"]])


plt.plot(x_1987f, y_1987f, marker='.', linestyle='none')
plt.plot(x_1987s, y_1987s, marker='.', linestyle='none')
plt.show()

#e
plt.plot(grant_1987.loc[grant_1987["species"]=="fortis" ,["beak depth (mm)"]], grant_1987.loc[grant_1987["species"]=="fortis" ,["beak length (mm)"]], marker='.', linestyle='none', color="b")
plt.plot(grant_1987.loc[grant_1987["species"]=="scandens" ,["beak depth (mm)"]], grant_1987.loc[grant_1987["species"]=="scandens" ,["beak length (mm)"]], marker='.', linestyle='none', color="r")
plt.show()


#4.2a
weight=pd.read_csv('data/bee_weight.csv', comment='#', header=0)
sperm=pd.read_csv('data/bee_sperm.csv', comment='#', header=0)

#b
c_weight=weight.loc[weight["Treatment"]=="Control" ,["Weight"]]
p_weight=weight.loc[weight["Treatment"]=="Pesticide" ,["Weight"]]
p_weight=p_weight.as_matrix()
c_weight=c_weight.as_matrix()
p_weight=p_weight.flatten()
c_weight=c_weight.flatten()
x_cont, y_cont = ecdf(c_weight)
x_pest, y_pest = ecdf(p_weight)
plt.plot(x_pest, y_pest, marker='.', linestyle='none')
plt.plot(x_cont, y_cont, marker='.', linestyle='none')
plt.show()
#ECDF not working here

#c
np.mean(c_weight)
np.mean(p_weight)

# Number of replicas
n_reps = 100000

# Initialize bootstrap replicas array
bs_c_weight = np.empty(n_reps)
bs_p_weight = np.empty(n_reps)

c_weight=weight.loc[weight["Treatment"]=="Control" ,["Weight"]]
p_weight=weight.loc[weight["Treatment"]=="Pesticide" ,["Weight"]]
p_weight=p_weight.as_matrix()
c_weight=c_weight.as_matrix()
p_weight=p_weight.flatten()
c_weight=c_weight.flatten()

# Compute replicates
for i in range(n_reps):
    bs_sample = np.random.choice(c_weight, replace=True, size=len(c_weight))
    bs_c_weight[i] = np.std(bs_sample)

conf_int_cont = np.percentile(bs_c_weight, [2.5, 97.5])


for i in range(n_reps):
    bs_sample = np.random.choice(p_weight, replace=True, size=len(p_weight))
    bs_p_weight[i] = np.std(bs_sample)

conf_int_pes = np.percentile(bs_p_weight, [2.5, 97.5])


#4.3a
