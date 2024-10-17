A = []
a = 0
k = 0
i = 0
while a != '':
    a = input()
    if a != '':
        A.append(int(a))
    else: break
C = []
for a in range(len(A)-1):
    y = A[a+1]    
    C.append(y)
for a in range(len(A)-1):
    if A[a] +1 == C[a]:
        k += 1
    if A[a] - 1 == C[a]:
        i += 1
if k >= i:
    r = k
else: r = i

print("максимальная длина упорядоченной последовательности",r + 1)
