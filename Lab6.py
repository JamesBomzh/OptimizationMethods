# Метод Ньютона многомерной минимизации

import sympy as sp
import math

x, y = sp.symbols('x, y')

J = x ** 3 + 8*y**3 - 6*x*y + 5

x0 = 1.0
y0 = 0.5

eps = 0.0001

while math.sqrt((J.diff(x) ** 2 + J.diff(y) ** 2).subs(x, x0).subs(y, y0)) >= eps:
    h = 1.0 / (J.diff(x, x) * J.diff(y, y) - J.diff(x, y) * J.diff(y, x))
    x0 = x0 - h * J.diff(x).subs(x, x0).subs(y, y0)
    y0 = y0 - h * J.diff(y).subs(y, y0).subs(x, x0)

print(x0, y0, J.subs(x, x0).subs(y, y0))
