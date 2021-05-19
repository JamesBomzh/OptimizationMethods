# Градиент. Метод дробления шага

import sympy as sp
import math

x, y = sp.symbols('x, y')

J = 2*x**3 + y**3 - x*y - 5

x0 = 0.3
y0 = 0.3
alpha = 1

eps = 0.0001

while math.sqrt((J.diff(x) ** 2 + J.diff(y) ** 2).subs(x, x0).subs(y, y0)) >= eps:
    x1 = x0 - alpha * J.diff(x).subs(x, x0).subs(y, y0)
    y1 = y0 - alpha * J.diff(y).subs(y, y0).subs(x, x0)
    J1 = J.subs(x, x1).subs(y, y1)
    J0 = J.subs(x, x0).subs(y, y0)
    print(J0)
    if J.subs(x, x1).subs(y, y1) < J.subs(x, x0).subs(y, y0):
        x0 = x1
        y0 = y1
        print(x0, y0)
    else:
        alpha /= 2

print(x0, y0, J.subs(x, x0).subs(y, y0))
