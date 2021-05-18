# Метод Ньютона одномерной минимизации

import sympy as s


def valuePoint(func, wow):
    value = func.subs(x, wow)
    return value


def funcDif(wow):
    diffur = s.diff(3*x**4 + x**3 + x**2 + 3*x + 2, x, wow)
    return diffur


x0 = 0.5
eps = 0.001
x = s.Symbol('x')
deriv = valuePoint(funcDif(1), x0)

while abs(deriv) > eps:
    x0 -= (valuePoint(funcDif(1), x0)) / (valuePoint(funcDif(2), x0))
    deriv = valuePoint(funcDif(1), x0)
print("x =", x0, "y =", valuePoint(funcDif(0), x0))
