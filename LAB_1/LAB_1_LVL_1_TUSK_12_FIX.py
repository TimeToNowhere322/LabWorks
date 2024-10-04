x = int(input('Введите Х'))
z = 0
for i in range(0,11):
	s = 1 / x**i
	z += s
print('Сумма прогрессии',z)