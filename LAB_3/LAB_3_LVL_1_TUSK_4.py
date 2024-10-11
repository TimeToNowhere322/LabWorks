A = [int(input()) for i in range(5)]
s = sum(A)/len(A)
B = [i - s for i in A]
print('Изначальный список')
print(A)
print('Среднее значение')
print(s)
print('Измененный список')
print(B)
