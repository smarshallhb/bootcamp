import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Specify parameters
n_gen = 16
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

ai_samples = np.random.binomial(n_cells, r, size=100000)

# Plot histogram, but it's a probability mass function, so no need for bins
plt.plot(np.arange(len(counts)), marker='.', markersize=10,
        linestyle='None')

plt.xlabel('Number of survivors')
plt.ylabel('Probability')
plt.xticks(np.arange(ai_samples.max()+1));
plt.margins(0.02)
plt.show()



print("Mean:", np.mean(ai_samples))
print("std:", np.std(ai_samples))
print("Fano:", np.var(ai_samples)/ np.mean(ai_samples))



def draw_random_mutation(n_gen,r):
    n_mut=0

    for g in range(n_gen):
        n_mut=2*n_mut + np.random.binomial(2**g-2*n_mut,r)

    return n_mut
