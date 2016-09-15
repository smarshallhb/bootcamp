#boocamp utils
import numpy as np
def ecdf(data):
    """calculate ecdf"""
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / float(len(x))
    return x, y


def draw_bs_reps(data, func, reps=1):
    """
    draws bs replicates from dataset
    """
    bs_replicates = np.empty(reps)
    for i in range(reps):
        bs = np.random.choice(data, replace=True, size=len(data))
        bs_replicates[i] = np.mean(bs)
    return func(bs_replicates)
