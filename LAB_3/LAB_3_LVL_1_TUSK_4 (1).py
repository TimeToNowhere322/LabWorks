A = []
B = []
C = []
a = 0
k = 0
i = 0
while a != '':
    a = input()
    if a != '':
        A.append(int(a))
    else:
        B.append(a)
        break
for a in A:
    C = [a + 1 for a in A]
    if C[0] - A[0] == a:
        k += 1

print(A, C, k)


