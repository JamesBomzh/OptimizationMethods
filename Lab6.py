# Метод Ньютона многомерной минимизации

import sympy as sp
import numpy as np
import math
from sympy.matrices import *

x, y = sp.symbols('u1, u2')

J = x ** 2 + 6 * x + y ** 2

x0 = 1.0
y0 = 0.5

eps = 0.000001

while math.sqrt((J.diff(x) ** 2 + J.diff(y) ** 2).subs(x, x0).subs(y, y0)) >= eps:
    lmd = 1.0 / (J.diff(x, x) * J.diff(y, y) - J.diff(x, y) * J.diff(y, x))
    x0 = x0 - lmd * J.diff(x).subs(x, x0)
    y0 = y0 - lmd * J.diff(y).subs(y, y0)

print(x0, y0, x0 ** 2 + 6 * x0 + y0 ** 2)
