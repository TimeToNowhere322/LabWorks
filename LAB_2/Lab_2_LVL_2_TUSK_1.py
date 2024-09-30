n0 = int(input())
n = 0
A = []
B = []
while n < n0:
    s = input()
    if s == "m":
        hm = int(input())
        A.append(hm)
    else:
        hf = int(input())
        B.append(hf)
    n += 1

print((sum(A) / len(A)), (sum(B) / len(B)))

'''from random import *
seed(15)
x1=randint(1,10)
x2=randint(1,13)
x3=randint(1,13)
print(x1,x2,x3)'''