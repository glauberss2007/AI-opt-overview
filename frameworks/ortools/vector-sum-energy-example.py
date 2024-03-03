# Import necessary libraries
import pandas as pd
import numpy as np
import ortools.linear_solver.pywraplp as otlp

## Inputs
# Read input data from Excel sheets into pandas DataFrames
data_generators = pd.read_excel('../../files/energy_inputs_dados.xlsx', sheet_name='geracao')
data_demands = pd.read_excel('../../files/energy_inputs_dados.xlsx', sheet_name='carga')
data_dependences = pd.read_excel('../../files/energy_inputs_dados.xlsx', sheet_name='dependencia')

# Calculate the number of generators
number_of_gens = len(data_generators)

# Create an LP solver instance using GLOP linear programming
solver = otlp.Solver('teste', otlp.Solver.GLOP_LINEAR_PROGRAMMING)

# Inputs
# Initialize Pg (power generated) variables as continuous variables within specified bounds
Pg = np.zeros(number_of_gens).tolist()
for g in range(number_of_gens):
    Pg[g] = solver.NumVar(0, float(data_generators.maximo[g]), 'Pg[{}]'.format([g]))

# Constraints
# Ensure that the total power generated equals the total demand
solver.Add(sum([Pg[g] for g in range(number_of_gens)]) == sum(data_demands.valor))
# Ensure that the power generated for each dependence is sufficient
for c in data_dependences.carga.unique():
    solver.Add(float(data_demands.valor[c]) <= sum([Pg[g] for g in data_dependences.gerador[data_dependences.carga == c]]))

# Objective Function
# Minimize the total cost, which is the sum of the power generated multiplied by the cost for each generator
solver.Minimize(sum(Pg[g] * float(data_generators.custo[g]) for g in range(number_of_gens)))

# Solve the linear programming model
results = solver.Solve()

# Check if an optimal solution is found
if results == otlp.Solver.OPTIMAL:
    print('Optimal solution found')
    # Print the optimal objective value
    print('Optimal Objective Value: %.2f' % solver.Objective().Value())
else:
    print('Optimal solution not found')

# Print the values of power generated for each generator in the optimal solution
for g in range(number_of_gens):
    print('Pg[%i] = %.2f' % (g, Pg[g].solution_value()))
