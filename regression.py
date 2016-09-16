import numpy as np
import pandas as pd

# We'll use scipy.optimize.curve_fit to do the nonlinear regression
import scipy.optimize

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


df = pd.read_csv('data/bcd_gradient.csv', comment='#')

df = df.rename(columns={'fractional distance from anterior': 'x',
                        '[bcd] (a.u.)': 'I_bcd'})

def bcd_gradient_model(x, I_0, a, lam):
    """Model for Bcd gradient: exponential decay plus background"""

    assert np.all(np.array(x) >= 0), 'All values of x must be >= 0.'
    assert np.all(np.array([I_0, a, lam]) >= 0), 'All parameters must be >= 0.'

    return a + I_0 * np.exp(-x / lam)

I_0_guess = 0.9
a_guess = 0.2
lam_guess = 1.0

def bcd_gradient_model_log_params(x, log_I_0, log_a, log_lam):
    """
    Model for Bcd gradient: exponential decay plus
    background with log parameters.
    """

    # Exponentiate parameters
    I_0, a, lam = np.exp(np.array([log_I_0, log_a, log_lam]))
    
    return bcd_gradient_model(x, I_0, a, lam)


# Construct initial guess array
log_p0 = np.log(p0)

# Do curve fit, but dump covariance into dummy variable
log_p, _ = scipy.optimize.curve_fit(bcd_gradient_model_log_params,
                                    df['x'], df['I_bcd'], p0=log_p0)

# Get the optimal parameter values
p = np.exp(log_p)

# Print the results
print("""
I_0 = {0:.2f}
  a = {1:.2f}
  λ = {2:.2f}
""".format(*tuple(p)))
