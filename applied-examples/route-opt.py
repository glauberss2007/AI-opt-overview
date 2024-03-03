# Importing necessary libraries
import pandas as pd  # Pandas is a data manipulation library
import numpy as np  # NumPy is a library for numerical operations in Python
from ortools.sat.python import cp_model  # ortools is a Google Optimization Tools library for constraint programming

# Reading input data from Excel files
nos = pd.read_excel('../files/rotas_input.xlsx', sheet_name='nos')  # Nodes data
caminhos = pd.read_excel('../files/rotas_input.xlsx', sheet_name='caminhos')  # Paths data
n_nos = len(nos)
n_caminhos = len(caminhos)

# Creating a constraint programming model
model = cp_model.CpModel()

# Creating binary decision variables x for each path
x = np.zeros(n_caminhos).tolist()
for c in caminhos.index:
    x[c] = model.NewIntVar(0, 1, 'x[{}]'.format([c]))

# Defining the objective function to minimize the total distance
model.Minimize(sum([x[c] * caminhos.distancia[c] for c in caminhos.index]))

# Adding constraints to ensure that one path leaves the origin and one path reaches the destination
no_origem = int(nos.no[nos.desc == 'origem'])
no_destino = int(nos.no[nos.desc == 'destino'])
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_de == no_origem]]) == 1)
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_para == no_destino]]) == 1)

# Adding constraints for intermediate nodes (desc=='meio')
for no in nos.no[nos.desc == 'meio']:
    sum_entra = sum([x[c] for c in caminhos.index[caminhos.no_para == no]])
    sum_sai = sum([x[c] for c in caminhos.index[caminhos.no_de == no]])
    model.Add(sum_sai <= 1)
    model.Add(sum_entra <= 1)
    model.Add(sum_entra == sum_sai)

# Solving the optimization problem using the CP-SAT solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Printing the status and objective value of the optimization
print('Status =', solver.StatusName(status))
print('FO =', solver.ObjectiveValue())

# Displaying the activated paths in the solution
caminhos['ativado'] = 0
for c in caminhos.index:
    caminhos.ativado[c] = solver.Value(x[c])
print(caminhos)

# Printing the chosen route
print('Rota escolhida')
for c in caminhos.index[caminhos.ativado == 1]:
    print('X%i%i - %.2f' % (caminhos.no_de[c], caminhos.no_para[c], caminhos.distancia[c]))
