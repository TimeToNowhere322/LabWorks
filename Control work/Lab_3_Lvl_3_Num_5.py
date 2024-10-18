from more_itertools import interleave
Gen = []
C = []
a = 0
k = 0
i = 0
while a != '':
    a = input()
    if a != '':
        Gen.append(int(a))
    else: break

Chet = sorted(Gen[::2])
Nchet = Gen[1::2]

print(list(interleave(Chet, Nchet)))
