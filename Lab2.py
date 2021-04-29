# Метод золотого сечения

import numpy as np

a0 = 0  # Задаём коэффициенты многочлена
a1 = 0
a2 = 0
a3 = 1
a4 = 2
a5 = 1


def J(u):
    return a0 * (u ** 5) + a1 * (u ** 4) + a2 * (u ** 3) + a3 * (u ** 2) + a4 * u + a5


print("Введите отрезок [a,b] ")
a = int(input())
b = int(input())
eps = 0.0001
alpha = (np.sqrt(5) - 1) / 2
beta = (3 - np.sqrt(5)) / 2
u1 = a + beta * (b - a)
u2 = a + alpha * (b - a)

while abs(b - a) >= eps:
    J1 = J(u1)
    J2 = J(u2)
    if J1 < J2:
        b = u2
        u2 = u1
        u1 = a + beta * (b - a)
    elif J1 > J2:
        a = u1
        u1 = u2
        u2 = a + alpha * (b - a)
    else:
        b = u2
        a = u1
        u1 = a + beta * (b - a)
        u2 = a + alpha * (b - a)

u0 = (b + a) / 2
J0 = J(u0)
print("u.=", u0)
print("J.=", J0)
print()
