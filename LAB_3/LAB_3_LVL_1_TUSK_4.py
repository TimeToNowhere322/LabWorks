'''from random import *
seed(15)
x1 = randint(1, 15)
x2 = randint(1, 20)
x3 = randint(1,14 )
print(x1, x2,x3)'''

A = []
B = []
n1 = int(input())
A.append(n1)
n2 = int(input())
A.append(n2)
n3 = int(input())
A.append(n3)
n4 = int(input())
A.append(n4)
n5 = int(input())
A.append(n5)
s = sum(A)/len(A)
n1 = n1 - s
B.append(n1)
n2 = n2 - s
B.append(n2)
n3 = n3 - s
B.append(n3)
n4 = n4 - s
B.append(n4)
n5 = n5 - s
B.append(n5)
print(B)