from  math import  *
sum = 0
x = int(input())
for i in range (1, 10):
    sum += cos(i*x) / (x**(i-1))
print("Сумма членов прогрессии при х =",x,"Равна",sum)