# Метод парабол

import math as m


def f(x):
    f = 4*m.sin(x) - 3*m.cos(x)
    return f


e = 0.0001

a = -3
b = 3
c = (a + b) / 2
ya = f(a)
yb = f(b)
yc = f(c)
N = 0

while (b - a > 2 * e):
    s = c + 0.5 * ((b - c) * (b - c) * (ya - yc) - (c - a) * (c - a) * (yb - yc)) / (
            (b - c) * (ya - yc) + (c - a) * (yb - yc))
    if (s == c):
        t = (a + c) / 2
    else:
        t = s
        yt = f(t)
        N = N + 1

    if (t < c):
        if (yt < yc):
            b = c
            yb = yc
            c = t
            yc = yt
        else:
            if (yt > yc):
                a = t
                ya = yt
            else:
                a = t
                ya = yt
                b = c
                yb = yc
                c = (a + b) / 2
                yc = f(c)
                N = N + 1
    else:
        if (t > c):
            if (yt < yc):
                a = c
                ya = yc
                c = t
                yc = yt
            else:
                if (yt > yc):
                    b = t
                    yb = yt
                else:
                    a = c
                    ya = yc
                    b = t
                    yb = yt
                    c = (a + b) / 2
                    yc = f(c)
                    N = N + 1
x = (a + b) / 2
y = f(x)

print("x = ", x)
print("y = ", y)
#  print("Kol-vo tochek: ", N)
