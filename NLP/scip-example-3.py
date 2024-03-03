# Import the Model class from PySCIPOpt
from pyscipopt import Model

# Create a PySCIPOpt model named 'example-1'
model = Model('example-1')

# Add decision variables 'x', 'y', and 'z' to the model
x = model.addVar('x')
y = model.addVar('y')
z = model.addVar('z')

# Set the objective function to maximize 'z'
model.setObjective(z, sense='maximize')

# Add a linear constraint to the model: z = x + y * x
model.addCons(z == x + y * x)

# Add additional linear constraints to the model
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
