#Метод Ньютона многомерной минимизации

import sympy as sp
import math as mp
from sympy.matrices import *

def Jux(func, dJdU,  num): #значение функции в точке минимума
  return func.subs(dJdU, num)

def Dif(f, var, num): #частные производные
  return sp.diff(f, var, num)

def grad(f, x, y, num, power): #градиент функции
  return Jux(Jux(Dif(f, x,power), x, num), y, num)

eps = 1  #Шаг 1: задаём требуемую точность > 0,
alpha = 0.01  #начальный шаг > 0
u0 = 1  #выбираем u0
 
x = sp.Symbol('x')
y = sp.Symbol('y')

f = x**2+x*y+y**2-x

gradf = grad(f, x, y, u0, 1) + grad(f, y, x, u0, 1) #Шаг 2: находим graddJ(u0)
gradNorm = mp.sqrt((grad(f, x, y, u0, 1))**2 + (grad(f, y, x, u0, 1))**2) #Находим ||grad J(u0)|| для проверки критерия остановки метода
H = Matrix(([grad(f, x, y, u0, 2),grad(Dif(f,y,1),x,y,u0,1)],[grad(Dif(f,x,1),y,x,u0,1),grad(f, y, x, u0, 2)]))

while (gradNorm >= eps):    #Пока критерий остановки метода ||grad J(u0)|| < eps не выполнен, делаем следубщие шаги:
  u1 = u0 - alpha*gradf*((H.inv()).det())  #Шаг 3: Полагаем, что u1 = u0 - alpha*gradJ(u0)*H(-1)
  Ju1 = grad(f, x, y, u1, 0)
  Ju0 = grad(f, x, y, u0, 0)
  if(Ju1 < Ju0 ): #Если J(u1) < J(u0), то полагаем следующее:
    u0 = u1 #u0 = u1
    Ju0 = Ju1   #J(u0) = J(u1), переходим к шагу 2.
  else: #Еcли J(u1) < J(u0), то уменьшаем начальный шаг в два раза и перехлим к шагу 3.
    alpha /= 2
    gradf = grad(f, x, y, u0, 1) + grad(f, y, x, u0, 1) #Шаг 2: находим gradJ(u0)
    gradNorm = mp.sqrt((grad(f, x, y, u0, 1))**2 + (grad(f, y, x, u0, 1))**2) #Находим ||grad J(u0)|| для проверки критерия остановки метода
    H = Matrix(([grad(f, x, y, u0, 2),grad(Dif(f,y,1),x,y,u0,1)],[grad(Dif(f,x,1),y,x,u0,1),grad(f, y, x, u0, 2)]))

print("u0=", u0)
print("gradFunc=", grad(f, x, y, u0, 0))