# Importing necessary libraries
import numpy as np
from pyswarm import pso


# Objective function to be optimized
def model_obj(x):
    # Initialize penalty variable
    pen = 0

    # Round the first variable to the nearest integer
    x[0] = np.round(x[0], 0)

    # Check and penalize if constraint is violated
    if not -x[0] + 2 * x[1] * x[0] <= 8:
        pen = np.inf
    if not 2 * x[0] + x[1] <= 14:
        pen = np.inf
    if not 2 * x[0] - x[1] <= 10:
        pen = np.inf

    # Calculate the objective function value with penalties
    return -(x[0] + x[1] * x[0]) + pen


# Constraint function (currently empty)
def cons(x):
    return []


# Define lower and upper bounds for variables
lb = [0, 0]
ub = [10, 10]

# Initial guess for the optimization
x0 = [0, 0]

# Perform particle swarm optimization
xopt, fopt = pso(model_obj, lb, ub, x0, cons)

# Print the optimized variables
print('Optimal x = ', xopt[0])
print('Optimal y = ', xopt[1])