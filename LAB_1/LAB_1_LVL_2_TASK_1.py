from math import *
A = []
for x in range(1,1000):
    n = 1
    s = (((cos(n * x))) / (n ** 2))
    n += 1
    A.append(s)
    if abs(sum(A)) < 0.0001:
        print(sum(A), A)
        break