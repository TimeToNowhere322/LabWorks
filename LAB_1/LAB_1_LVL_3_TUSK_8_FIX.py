from math import *
x = 0.05

while x < 1:
    x += 0.05
    y = e**(2 * x)
    i = 0
    z = 1
    s = 0
    while abs(z) > 0.0001:
        z = ((2 * x) ** i) / factorial(i)
        i += 1
        s += z

    print(round(x,2),round(y, 4),round(s, 4))
print('X   ', 'Y     ', 'Сумма выражения')
