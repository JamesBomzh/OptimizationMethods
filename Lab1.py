# Метод деления отрезка пополам

import random

a0 = 0  # Задаём коэффициенты многочлена
a1 = 0
a2 = 0
a3 = 1
a4 = 2
a5 = 1


def J(u):
    return a0 * (u ** 5) + a1 * (u ** 4) + a2 * (u ** 3) + a3 * (u ** 2) + a4 * u + a5


n = 0  # Шаг 1: Задаём n = 0, a, b, delta, eps
print("Введите отрезок [a,b] ")
a = int(input())
b = int(input())
eps = 0.0001

while abs(b - a) >= eps:  # Если условие не выполняется, переходим к шагу 5
    n += 1  # Шаг 2: Задаём n = n + 1, u1, u2
    delta = random.uniform(0, (b - a) / 2)
    u1 = (b + a - delta) / 2
    u2 = (b + a + delta) / 2
    J1 = J(u1)  # Шаг 3: Вычисляем J1 и J2
    J2 = J(u2)
    if J1 < J2:  # Шаг 4: Сравниваем J1 и J2
        b = u2
    elif J1 > J2:
        a = u1
    else:
        b = u2
        a = u1

u0 = (b + a) / 2  # Шаг 5: Вычисляем u. и J.
J0 = J(u0)
print("u.=", u0)
print("J.=", J0)
print()
