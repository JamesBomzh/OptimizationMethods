import math
import sympy as sp

x, y = sp.symbols('x, y')

eps = 0.0001
k = 0
r = 1

J = (x - 3) ** 2 + (y - 2) ** 2
g = (x + y - 4) ** 2
P = J + r * g


x0 = 1
y0 = 1


while math.sqrt((P.diff(x) ** 2 + P.diff(y) ** 2).subs(x, x0).subs(y, y0)) >= eps:
    h = 1.0 / (P.diff(x, x) * P.diff(y, y) - P.diff(x, y) * P.diff(y, x)).subs(x, x0).subs(y, y0)
    x0 = x0 - h * P.diff(x).subs(x, x0).subs(y, y0)
    y0 = y0 - h * P.diff(y).subs(x, x0).subs(y, y0)
    k += 1
    r /= 10
    P = J + r * g

print(x0, y0)
print(P.subs(x, x0).subs(y, y0))
