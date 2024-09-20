from math import *
A  = []
x = 0.1
s = 1
i = 0
y = 1
while abs(y) > 0.0001 and x <= 0.5:
    y = (((-1) ** i) * (x ** (2 * i + 1) / (2 * i + 1)))
    A.append(y)
    s = sum(A)
    print(x,y,sum(A))
    i += 1
    x += 0.05