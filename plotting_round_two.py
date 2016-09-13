import numpy as np
import scipy.special

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


# The x-values we want
x = np.linspace(-15, 15, 400)

# The normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')
plt.show()
