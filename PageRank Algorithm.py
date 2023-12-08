
import numpy as np
import np.linalg as la
np.set_printoptions(suppress = True)

def generate_internet(n) :
    c = np.full([n,n], np.arange(n))
    c = (abs(np.random.standard_cauchy([n,n])/2) > (np.abs(c - c.T) + 1)) + 0
    c = (c+1e-10) / np.sum((c+1e-10), axis=0)
    return c

def PageRank(c, d) :
    n = c.shape[0]
    r = 100 * np.ones(n) / n
    M = (d * c) + ((1-d) * np.ones([n, n]) / n)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01:
        lastR = r
        r = M @ r
        i += 1
    print(str(i), "iterations to convergence. ")
    return r
