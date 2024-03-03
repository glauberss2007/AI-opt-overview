# Import the Gurobi library
from gurobipy import *

# Create a Gurobi Model object named 'example1'
model = Model('example1')

# Add decision variables 'x' and 'y' to the model with their objective coefficients
x = model.addVar(obj=1, vtype='C', name='x')
y = model.addVar(obj=1, vtype='C', name='y')

# Update the model after adding variables
model.update()

## Constraints passed using 3 different ways

# Add the constraint: -x + 2y <= 8
model.addLConstr(-x + 2*y <= 8)

# Add the constraint: 2x + y <= 14
model.addLConstr(2*x + y, "<", 14)

# Create a linear expression L3 = 2x - y
L3 = LinExpr([2, -1], [x, y])

# Add the constraint: L3 <= 10
model.addLConstr(L3, "<", 10)

# Set the optimization sense: -1 for maximization and +1 for minimization
model.ModelSense = -1

# Optimize the model
model.optimize()

# Print the optimal values of decision variables 'x' and 'y'
print('x = ', x.X)
print('y = ', y.X)
