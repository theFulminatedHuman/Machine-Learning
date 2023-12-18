# PACKAGE
import matplotlib.pyplot as plt

import numpy as np

# GRADED FUNCTION

# This is the Gaussian function.
def f (x,mu, sig) :
    return np.exp(-(x-mu) **2/(2*sig**2)) / np.sqrt(2*np.pi) / sig

# Next up, the derivative with respect to μ.
# If you wish, you may want to express this as f(x, mu, sig) multiplied by chain rule terms.
# === COMPLETE THIS FUNCTION ===

def dfdmu (x, mu, sig) :
    return f(x, mu, sig) * ((x-mu) / sig**2)

# Finally in this cell, the derivative with respect to o.
# === COMPLETE THIS FUNCTION ===

def dfdsig (x,mu, sig):
    return f(x, mu, sig) * ((-1/sig) + ((x-mu)**2/sig**3))

def steepest_step (x, y, mu, sig, aggression):
  """
  Computes the steepest descent step for a Gaussian distribution.

  Args:
    x: A NumPy array containing the data points.
    y: A NumPy array containing the target values.
    mu: The current mean of the Gaussian distribution.
    sig: The current standard deviation of the Gaussian distribution.
    aggression: The learning rate of the steepest descent algorithm.

  Returns:
    A NumPy array containing the steepest descent step.
  """

  J = np.array([
      -2*(y - f(x,mu, sig)) @ dfdmu(x,mu, sig),
      -2*(y - f(x,mu, sig)) @ dfdsig(x,mu, sig)
  ])
  step = -J * aggression
  return step

# First get the heights data, ranges and frequencies
x, y = heights_data()

# Next we'll assign trial values for these.
mu = 155; sig = 6

# We'll keep a track of these so we can plot their evolution.
P = np.array([[mu, sig]])

# Plot the histogram for our parameter guess
histogram(f, [mu, sig])

# Do a few rounds of steepest descent.
for i in range(50):

    dmu, dsig = steepest_step(x, y, mu, sig, 2000)
    mu += dmu
# Plot the path through parameter space.

    sig += dsig
    p = np.append(p, [[mu, sig]], axis=0)

contour(f, p)
# Plot the final histogram.

histogram(f, [mu, sig])
