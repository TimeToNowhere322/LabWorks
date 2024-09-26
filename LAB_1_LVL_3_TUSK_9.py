from math import *
A  = []
x = 0.1
s = 1
i = 0
y = 1
z = 1
while x <= 0.5 and abs(z) > 0.0001:
    z = (((-1) ** i) * (x ** (2 * i + 1) / (2 * i + 1)))
    y = atan(x)
    A.append(z)
    s = sum(A)
    print(x,y,sum(A))
    i += 1
    x += 0.05
print(A)
