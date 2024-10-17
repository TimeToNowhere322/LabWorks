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
for a in range(len(A)-1):           # перебор элементов от индекса 1, до -2
    y = A[a+1]     # сосед слева от i + сосед справа от i
    C.append(y)
for a in range(len(A)-1):
    if A[a] +1 == C[a]:
        k += 1
    if A[a] - 1 == C[a]:
        i += 1
if k >= i:
    r = k
else: r = i
print(A, C,r + 1)
