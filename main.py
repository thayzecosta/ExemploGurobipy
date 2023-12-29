'''
Exemplo de uso do Gurobipy para resolver um problema de programacao linear

O problema a ser resolvido é o seguinte:

maximizar x + y
sujeito a
  -x + 2 * y <= 7
  2 * x + y <= 14
  2 * x - y <= 10
'''

# pip install gurobipy

from gurobipy import Model, LinExpr


model = Model('exemplo')

x = model.addVar(obj=1, vtype='C', name='x')
y = model.addVar(obj=1, vtype='C', name='y')

# obj indica o coeficiente da variável na função objetivo
# 'C' indica que a variável é contínua

model.update()

L1 = LinExpr([-1, 2], [x, y])
model.addLConstr(L1, "<", 8)

L2 = LinExpr([2, 1], [x, y])
model.addLConstr(L2, "<", 14)

L3 = LinExpr([2, -1], [x, y])
model.addLConstr(L3, "<", 10)

model.ModelSense = -1  # Indica que é uma maximização

model.optimize()

print('x=', x.X)
print('y=', y.X)
