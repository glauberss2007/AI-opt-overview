from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = model.NewIntVar(0, 1000, 'x')
y = model.NewIntVar(0, 1000, 'y')
z = model.NewIntVar(0, 1000, 'z')

model.Add(2*x+7*y+3*z<=50)
model.Add(3*x-5*y+7*z<=45)
model.Add(5*x+2*y-6*z<=37)

model.Maximize(2*x+2*y+3*z)

solver = cp_model.CpSolver()
status = solver.Solve(model)

print('Status:', solver.StatusName(status))
print('FO = ', solver.ObjectiveValue())
print('x = ', solver.Value(x))
print('y = ', solver.Value(y))
print('z = ', solver.Value(z))