a = int(input("введите коэффициент a квадратного уравнения"))
b = int(input("введите коэффициент b квадратного уравнения"))
c = int(input("введите коэффициент c квадратного уравнения"))
x1 = 0
x2 = 0
d = 0
if a == 0:
    x1 = -c/b
    print(x1)
elif b == 0:
    x1 = (-c/a)**0.5
    x2 = -(-c/a)**0.5
    print(x1)
    print(x2)
elif c == 0:
    x1 = -b/a
    print(x1)
    print(x2)
else:
    d = b*b - 4*a*c
    if d < 0:
        print("корней нет")
    elif d == 0:
        x1 = -b/(2*a)
        print(x1)
    elif d >0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print(x1)
        print(x2)