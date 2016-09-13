import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

rc = {'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)

xa_high = np.loadtxt('data/xa_high_food.csv', comments="#")
xa_low = np.loadtxt('data/xa_low_food.csv', comments="#")





bins = np.arange(1600, 2501, 50)

_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
# Add axis labels
plt.xlabel('Cross-sectional area',fontsize=18)
plt.ylabel("count", fontsize=18, rotation="horizontal" )
plt.legend(('low', 'high'), loc='upper right')
plt.show()
