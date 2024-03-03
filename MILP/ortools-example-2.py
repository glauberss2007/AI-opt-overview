# Import the linear solver module from OR-Tools
import ortools.linear_solver.pywraplp as otlp

# Create a linear programming solver object (GLOP_LINEAR_PROGRAMMING)
solver = otlp.Solver('test', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create integer decision variable 'x' with bounds (0, 10)
x = solver.IntVar(0, 10, 'x')

# Create continuous decision variable 'y' with bounds (0, 10)
y = solver.NumVar(0, 10, 'y')

# Add linear constraints to the solver
solver.Add(-x + 2 * y <= 7)
solver.Add(2 * x + y <= 14)
solver.Add(2 * x - y <= 10)

# Set the objective function to maximize (x + y)
solver.Maximize(x + y)

# Solve the linear programming problem
result = solver.Solve()

# Check if an optimal solution is found
if result == otlp.Solver.OPTIMAL:
    print('Optimal solution found')
else:
    print('Optimal solution not found')

# Print the optimal values of decision variables 'x' and 'y'
print('x = ' + str(x.SolutionValue()))
print('y = ' + str(y.SolutionValue()))
