import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')


def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / float(len(data))

x_1975, y_1975 = ecdf(bd_1975)



plt.plot(x_1975, y_1975, marker='.', linestyle='none', color="blue")


bs_replicates = np.empty(100)
for i in range(100):
    bs = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates[i] = np.mean(bs)

x_1975_bs, y_1975_bs =ecdf(bs_replicates)

plt.plot(x_1975_bs, y_1975_bs,color="blue", alpha=.1, marker='.', linestyle='none')

plt.margins(0.02)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.show()
