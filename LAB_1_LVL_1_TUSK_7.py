'''Задание 7:
      Вычислить факториал шести'''
from math import *
A = []
for x in range(1, 7):
    x0 = 1
    y = x * x0
    x += 1
    A.append(y)
print(prod(A))