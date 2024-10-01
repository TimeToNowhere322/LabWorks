from math import *
x = 0.05

while x < 0.4:
    x += 0.05
    y = atan(x)
    i = 0
    z = 1
    s = 0
    while abs(z) > 0.0001:
        z = ( (-1) ** i ) * ( (round(x,2) ** (2 * i + 1) ) / (2 * i + 1) )
        i += 1
        s += z
        A.append(z)

    print(round(x,2),y,s)