#boocamp utils
import numpy as np
def ecdf(data):
    """calculate ecdf"""
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / float(len(x))
    return x, y
