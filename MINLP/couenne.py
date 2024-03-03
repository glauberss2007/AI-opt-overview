# Import necessary modules from Pyomo
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Create a concrete Pyomo model
model = pyo.ConcreteModel()

# Define integer decision variable 'x' within the set of integers with bounds (0, 10)
model.x = pyo.Var(within=Integers, bounds=(0, 10))

# Define continuous decision variable 'y' with bounds (0, 10)
model.y = pyo.Var(bounds=(0, 10))

# Alias for convenience
x = model.x
y = model.y

# Add constraints to the model
model.C1 = pyo.Constraint(expr=-x + 2 * y * x<= 7)
model.C2 = pyo.Constraint(expr=2 * x + y <= 14)
model.C3 = pyo.Constraint(expr=2 * x - y <= 10)

# Set the objective function to maximize (x + y)
model.obj = pyo.Objective(expr=x + y * x, sense=maximize)

# Choose the solver (GLPK in this case) and solve the optimization problem
opt = SolverFactory('couenne', executable='COUENNE_EXECUTABLE_PATH')
opt.solve(model)

# Print the details of the model (constraints, variables, objective function)
model.pprint()

# Retrieve the optimal values of decision variables 'x' and 'y'
x_value = pyo.value(x)
y_value = pyo.value(y)

# Print the optimal values of decision variables 'x' and 'y'
print('x =', x_value)
print('y =', y_value)
