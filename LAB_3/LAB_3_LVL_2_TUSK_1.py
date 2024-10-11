A = []
B = []
a = 0
while a != '':
    a = input()
    if a != '':
        A.append(int(a))
    else:
        B.append(a)
        break
z = min(A)
print('Удвоенное минимальное значение',z * 2)
