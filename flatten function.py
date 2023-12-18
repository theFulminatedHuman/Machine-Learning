import numpy as np

def reshape(x):
    """Return x_reshaped as a flattened vector of the multi-dimensional array x"""
    x_reshaped = np.array(x).flatten()
    return x_reshaped
