from math import *
A = []
x = float(input('Введите X'))
n = 1
s = (((cos(n * x))) / (n ** 2))
while abs(s) >= 0.0001:
    s = (((cos(n * x))) / (n ** 2))
    n += 1
    A.append(s)
print('Сумма прогрессии' ,sum(A))
