A = 1
B = 9
EPS = 0.01

def func(x, y):
    return A*x**2+B*y**2
def cond1(x, y):
    return C1_B*x+C1_B*y+C1_C

def cond2(x, y):    
    return C2_C-C2_A*x-C2_B*y

def check_condition(cond):
    return cond <= 0

C1, C2 = 1, 1
C1_A, C1_B, C1_C = 1, 2, 1
C2_A, C2_B, C2_C = -1, -1, 1

def gamma_gradient(x, y, gamma):
    if check_condition(cond1(x,y)) and check_condition(cond2(x,y)):
        return 2*A*x, 2*B*y
    elif not check_condition(cond1(x,y)) and check_condition(cond2(x,y)):
        return 2*A*x + 2*C1_A*C1*gamma*(C1_C + C1_A*x + C1_B*y), 2*B*y + 2*C1_B*C1*gamma*(C1_C + C1_A*x + C1_B*y)
    elif check_condition(cond1(x,y)) and not check_condition(cond2(x,y)):
        return 2*A*x + 2*gamma*C2_A*C2*(C2_C + C2_A*x + C2_B*y), 2*B*y + 2*gamma*C2_B*C2*(C2_C + C2_A*x + C2_B*y)
    else:
        return 2*(A*x + gamma*C1_A*C1*(C1_A*x + C1_B*y + C1_C) + gamma*C2_A*C2*(C2_A*x + C2_B*y + C2_C)), \
    2*(B*y + gamma*C1_B*C1*(C1_A*x + C1_B*y + C1_C) + gamma*C2_B*C2*(C2_A*x + C2_B*y + C2_C))

def vect_norm(x, y):
    return (x**2+y**2)**0.5

def step(gamma):
    return 2*max(A+gamma*(C1_A**2+C2_A**2), B+gamma*(C1_B**2+C2_B**2))

def gradient_descent(x, y, gamma):
    i = 0
    s = step(gamma) # получаем шаг
    a, b = gamma_gradient(x, y, gamma) # получаем градиент 
    while vect_norm(a, b) > EPS:
        x, y = x - a/s, y - b/s
        a, b = gamma_gradient(x, y, gamma)
        i += 1
    return x, y, i
from random import uniform

def generate_point(a, b):
    for i in range(10):
        x = uniform(a, b)
        y = uniform(a, b)
        if not check_condition(cond1(x, y)) and not check_condition(cond2(x, y)):
            return x, y
    raise Exception('Bad point generated')
x, y = generate_point(-5, 5)
g = 1
values = '['

for i in range(1, 11):
    res = gradient_descent(x, y, g)
    values+="(%f, %f), " % (res[0], res[1])
    g*=2

values = values[:-2] + ']'

print(values[1:22])