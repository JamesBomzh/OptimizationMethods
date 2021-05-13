# Метод дробления шага

import sympy as sp
import math as mp


def Jux(func, dJdU, num):  # значение функции в точке минимума
    return func.subs(dJdU, num)


def Dif(var, num):  # частные производные
    return sp.diff(x ** 2 + y ** 2 - x - y + x * y, var, num)


def grad(x, y, num, power):  # градиент функции
    return Jux(Jux(Dif(x, power), x, num), y, num)


eps = 1  # Шаг 1: задаём требуемую точность > 0,
alpha = 0.01  # начальный шаг > 0
u0 = 1  # выбираем u0

x = sp.Symbol('x')
y = sp.Symbol('y')

gradf = grad(x, y, u0, 1) + grad(y, x, u0, 1)  # Шаг 2: находим gradJ(u0)
gradNorm = mp.sqrt((grad(x, y, u0, 1)) ** 2 + (
    grad(y, x, u0, 1)) ** 2)  # Находим ||grad J(u0)|| для проверки критерия остановки метода

while (gradNorm >= eps):  # Пока критерий остановки метода ||grad J(u0)|| < eps не выполнен, делаем следубщие шаги:
    u1 = u0 - alpha * gradf  # Шаг 3: Полагаем, что u1 = u0 - alpha*gradJ(u0)
    Ju1 = grad(x, y, u1, 0)
    Ju0 = grad(x, y, u0, 0)
    if (Ju1 < Ju0):  # Если J(u1) < J(u0), то полагаем следующее:
        u0 = u1  # u0 = u1
        Ju0 = Ju1  # J(u0) = J(u1), переходим к шагу 2.
    else:  # Еcли J(u1) < J(u0), то уменьшаем начальный шаг в два раза и перехлим к шагу 3.
        alpha /= 2
    gradf = grad(x, y, u0, 1) + grad(y, x, u0, 1)  # Шаг 2: находим gradJ(u0)
    gradNorm = mp.sqrt((grad(x, y, u0, 1)) ** 2 + (
        grad(y, x, u0, 1)) ** 2)  # Находим ||grad J(u0)|| для проверки критерия остановки метода

print("u0=", u0)
print("gradFunc=", grad(x, y, u0, 0))
