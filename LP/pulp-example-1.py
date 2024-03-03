# Import the PuLP library
import pulp as pl

# Create a linear programming problem with the name 'Ex' and the objective to maximize
model = pl.LpProblem('Ex', pl.LpMaximize)

# Define decision variables 'x' and 'y' with lower bound 0 and upper bound 10
x = pl.LpVariable('x', 0, 10)
y = pl.LpVariable('y', 0, 10)

# Add linear constraints to the model
model += -x + 2 * y <= 8
model += 2 * x + y <= 14
model += 2 * x - y <= 10

# Set the objective function to maximize (x + y)
model += x + y

# Solve the linear programming problem
status = model.solve()

# Retrieve the optimal values of decision variables 'x' and 'y'
x_value = pl.value(x)
y_value = pl.value(y)

# Print the optimal values of decision variables 'x' and 'y'
print('x = ', x_value)
print('y = ', y_value)
