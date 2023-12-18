import numpy as np
from scipy import optimize

# Define the functions and their derivatives
def f(x, y):
    return -np.exp(x - y**2 + x*y)

def g(x, y):
    return np.cosh(y) + x - 2

def dfdx(x, y):
    return -np.exp(x - y**2 + x*y) * (1 + y)

def dfdy(x, y):
    return -np.exp(x - y**2 + x*y) * (-2*y + x)

def dgdx(x, y):
    return 1

def dgdy(x, y):
    return -np.sinh(y)

# Lagrange multiplier method
def lagrange_multiplier(xy_lambda):
    x, y, _lambda = xy_lambda
    return np.array([
        dfdx(x, y) - _lambda * dgdx(x, y),
        dfdy(x, y) - _lambda * dgdy(x, y),
        -g(x, y)
    ])

# Initial guess
x0, y0, lambda0 = (0, 0, 0)

# Solve the system of equations using optimize.root
result = optimize.root(lagrange_multiplier, [x0, y0, lambda0])

# Extract the solution
x_min, y_min, lambda_min = result.x

# Display the results
print("Minimum x =", x_min)
print("Minimum y =", y_min)
print("Lambda =", lambda_min)
print("Minimum f(x, y) =", f(x_min, y_min))
