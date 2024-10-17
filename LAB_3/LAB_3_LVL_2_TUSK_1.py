A = []
a = 0
while a != '':
    a = input()
    if a != '':
        A.append(int(a))
    else:
        break
z = min(A)
print('Удвоенное минимальное значение',z * 2)
