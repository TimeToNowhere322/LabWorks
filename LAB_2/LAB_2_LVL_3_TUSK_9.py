A = []
B = []
r = 0
while r != '':
    r = input()
    if r != '':
        A.append(int(r))
    else:
        B.append(r)
        break

print(min(A))

