# Importing necessary libraries
import pyomo.environ as pyo  # Pyomo is a Python-based open-source optimization modeling language
import numpy as np  # NumPy is a library for numerical operations in Python
from pyomo.environ import *
from pyomo.opt import SolverFactory  # SolverFactory is used to create optimization solvers

# Creating a concrete model using Pyomo
model = pyo.ConcreteModel()

# Defining decision variables p and N with specified bounds
model.p = pyo.Var(bounds=(50, 200))
model.N = pyo.Var(within=Integers, bounds=(0, None))
p = model.p
N = model.N

# Defining the objective function to maximize, which is the product of p and N
model.obj = pyo.Objective(expr=p * N, sense=maximize)

# Adding a constraint to the model: N should equal 1001 - 5*p
model.C1 = pyo.Constraint(expr=N == 1001 - 5 * p)

# Creating an instance of the Gurobi solver
opt = SolverFactory('gurobi')

# Solving the optimization problem using the Gurobi solver
opt.solve(model)

# Printing the optimized values of p, N, and the product of p and N (receita)
print('p:', np.round(pyo.value(p), 2))
print('N:', np.round(pyo.value(N), 2))
print('receita:', pyo.value(p) * pyo.value(N))
