import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

rc = {'lines.linewidth':2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)

xa_high = np.loadtxt('data/xa_high_food.csv', comments="#")
xa_low = np.loadtxt('data/xa_low_food.csv', comments="#")

def ecdf(data):
    """calculate ecdf"""
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / float(len(x))
    return x, y

x_high, y_high= ecdf(xa_high)

plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20)
plt.show()
