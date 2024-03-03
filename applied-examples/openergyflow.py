# Importing necessary libraries
import pyomo.environ as pyo  # Pyomo is a Python-based open-source optimization modeling language
import numpy as np  # NumPy is a library for numerical operations in Python
import pandas as pd  # Pandas is a data manipulation library
from pyomo.environ import *
from pyomo.opt import SolverFactory  # SolverFactory is used to create optimization solvers

# Input data from Excel files
barras = pd.read_excel('../files/sist_eletrico.xlsx', sheet_name='barras')  # Bus data
geracao = pd.read_excel('../files/sist_eletrico.xlsx', sheet_name='geracao')  # Generation data
carga = pd.read_excel('../files/sist_eletrico.xlsx', sheet_name='carga')  # Load data
linha = pd.read_excel('../files/sist_eletrico.xlsx', sheet_name='linha')  # Transmission line data
Nb = len(barras)
Ng = len(geracao)
Nd = len(carga)
Nl = len(linha)

# Creating a concrete model using Pyomo
model = pyo.ConcreteModel()

# Defining decision variables for generation (Pg), load (Pl), and bus voltage angles (teta)
model.Pg = pyo.Var(range(Ng))
model.Pl = pyo.Var(range(Nl))
model.teta = pyo.Var(range(Nb), bounds=(-np.pi, np.pi))
Pg = model.Pg
Pl = model.Pl
teta = model.teta

# Defining the objective function to minimize the total generation cost
model.obj = pyo.Objective(expr=sum([Pg[g] * geracao.custo[g] for g in geracao.index]), sense=minimize)

# Power balance constraints for each bus
model.balanco = pyo.ConstraintList()
for n in barras.index:
    sum_Pg = sum([Pg[g] for g in geracao.index[geracao.barra == n]])
    sum_Pls = sum([Pl[l] for l in linha.index[linha.barra_de == n]])
    sum_Plr = sum([Pl[l] for l in linha.index[linha.barra_para == n]])
    sum_Pd = sum([carga.carga[d] for d in carga.index[carga.barra == n]])
    model.balanco.add(expr=sum_Pg - sum_Pls + sum_Plr == sum_Pd)

# Power flow constraints for each transmission line
model.fluxo = pyo.ConstraintList()
for l in linha.index:
    Bl = linha.Bl[l]
    n_send = linha.barra_de[l]
    n_rec = linha.barra_para[l]
    delta_teta = teta[n_send] - teta[n_rec]
    model.fluxo.add(expr=Pl[l] == Bl * delta_teta)

# Generator limits
model.limger = pyo.ConstraintList()
for g in geracao.index:
    model.limger.add(inequality(0, Pg[g], geracao.pgmax[g]))

# Power flow limits
model.limflux = pyo.ConstraintList()
for l in linha.index:
    model.limflux.add(inequality(-linha.plmax[l], Pl[l], linha.plmax[l]))

# Reference bus constraint
model.ref = pyo.Constraint(expr=teta[0] == 0)

# Solving the optimization problem using the Gurobi solver
opt = SolverFactory('gurobi')
opt.solve(model)

# Displaying the optimization results
model.pprint()
