# Import necessary libraries
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# Define the objective function 'f' to be optimized
def f(x):
    pen = 0  # Penalty for infeasible solutions
    # Check constraints and apply penalty if violated
    if not -x[0] + 2*x[1] * x[0] <= 8:
        pen = np.inf
    if not 2*x[0] + x[1] <= 14:
        pen = np.inf
    if not 2*x[0] - x[1] <= 10:
        pen = np.inf
    # Return the negation of the objective function with penalty
    return -(x[0] + x[1] * x[0]) + pen

# Define variable bounds and types for the genetic algorithm
varbounds = np.array([[0, 10], [0, 10]])  # Variable bounds for each dimension
vartype = np.array([['int'], ['real']])  # Variable types (integer or real) for each dimension

# Create a genetic algorithm model
model = ga(function=f, dimension=2, variable_type_mixed=vartype, variable_boundaries=varbounds)

# Run the genetic algorithm optimization
model.run()
