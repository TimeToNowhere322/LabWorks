key = 0
Ssq = []
Scr = []
Str = []
while key != '':
    key = input()
    a = input()
    b = input()
    if key  == 'пу':
        p1 = int(a)*int(b)
        Ssq.append(p1)
    if key == 'пк':
        p2 = 3.14 * (((int(a)+int(b))**2)/4)
        Scr.append(p2)
    if key == 'пт':
        p3 = (0.5*int(a))*(int(b)**2 - (int(a)**2/4))**0.5
        Str.append(p3)
print("Площади прямоугольников", Ssq)
print("Площади колец", Scr)
print("Площади треугольников",Str)