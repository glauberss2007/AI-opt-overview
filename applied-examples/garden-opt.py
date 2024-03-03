# Importing necessary libraries
import pyomo.environ as pyo  # Pyomo is a Python-based open-source optimization modeling language
import numpy as np  # NumPy is a library for numerical operations in Python
from pyomo.environ import *
from pyomo.opt import SolverFactory  # SolverFactory is used to create optimization solvers

# Creating a concrete model using Pyomo
model = pyo.ConcreteModel()

# Defining decision variables x and y with non-negative bounds
model.x = pyo.Var(bounds=(0, None))
model.y = pyo.Var(bounds=(0, None))
x = model.x
y = model.y

# Defining the objective function to maximize, which is the product of x and y
model.obj = pyo.Objective(expr=x * y, sense=maximize)

# Adding a constraint to the model: 2*x + y should be less than or equal to 100
model.c1 = pyo.Constraint(expr=2 * x + y <= 100)

# Creating an instance of the Gurobi solver
opt = SolverFactory('gurobi')

# Solving the optimization problem using the Gurobi solver
opt.solve(model)

# Printing the optimized values of x, y, and the product of x and y
print('x:', np.round(pyo.value(x), 2))
print('y:', np.round(pyo.value(y), 2))
print('A:', np.round(pyo.value(x) * pyo.value(y), 2))
