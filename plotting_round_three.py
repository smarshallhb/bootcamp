import numpy as np
import scipy.stats

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

data_txt = np.loadtxt('collins_switch.csv', delimiter=',', skiprows=2)

iptg=data_txt[:,0]
gfp=data_txt[:,1]
sem=data_txt[:,2]


plt.plot(iptg,gfp,  marker='.', linestyle='none', markersize=10)

plt.errorbar(iptg,gfp,xerr=None,yerr=sem, linestyle='none', markersize=10)
plt.xscale('log')
plt.show()
