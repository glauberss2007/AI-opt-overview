# Import the Model class from PySCIPOpt
from pyscipopt import Model

# Create a PySCIPOpt model named 'example-1'
model = Model('example-1')

# Add decision variables 'x' and 'y' to the model
x = model.addVar('x',vtype='INTEGER')
y = model.addVar('y')
z = model.addVar('z')

# Set the objective function to maximize (x + y)
model.setObjective(z, sense='maximize')

# Workaround to fix NL FO scip error
model.addCons(z == x + y * x)

# Add linear constraints to the model
model.addCons(-x + 2 * y * x <= 8)
model.addCons(2 * x + y <= 14)
model.addCons(2 * x - y <= 10)

# Optimize the model
model.optimize()

# Retrieve the optimal solution
sol = model.getBestSol()

# Print the optimal values of decision variables 'x' and 'y'
print('x = ', sol[x])
print('y = ', sol[y])