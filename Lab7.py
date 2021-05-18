import math
import sympy as sp
import numpy as np

u1, u2 = sp.symbols('u1, u2')

eps = 0.0001
k = 0
r = 1

J = (u1 - 3) ** 2 + (u2 - 2) ** 2
g = (u1 + u2 - 4) ** 2
P = J + r * g

a1 = 1
a2 = 1

u1i = a1
u2i = a2


while math.sqrt((P.diff(u1) ** 2 + P.diff(u2) ** 2).subs(u1, u1i).subs(u2, u2i)) >= eps:
    lmd = 1.0 / (P.diff(u1, u1) * P.diff(u2, u2) - P.diff(u1, u2) * P.diff(u2, u1)).subs(u1, u1i).subs(u2, u2i)
    u1i = u1i - lmd * P.diff(u1).subs(u1, u1i).subs(u2, u2i)
    u2i = u2i - lmd * P.diff(u2).subs(u1, u1i).subs(u2, u2i)
    k += 1
    r /= 10
    P = J + r * g
    # print(u1i, u2i, lmd)

print(u1i, u2i)
print(P.subs(u1, u1i).subs(u2, u2i))
