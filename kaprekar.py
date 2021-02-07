def numerics(n): #преобразование числа в список цифр
    s = str(n)
    return([int(x) for x in s])

def kaprekar_step(L): #шаг преобразования
    return(int((str(list(reversed(sorted(L))))).strip("[]").replace(", ","")) - int((str(sorted(L))).strip("[]").replace(", ","")))

def kaprekar_check(n): #проверка, может ли данное число использоваться для преобразования
    x = len(str(n))
    if x in [3, 4, 6] and n not in [100, 1000, 100000] and len(set(numerics(n))) > 1:
        return(True)
    else:
        return(False)

def kaprekar_loop(n):
    cash = []
    while n not in cash:
        if kaprekar_check(n):
            cash.append(n)
            n = kaprekar_step( numerics(n))
        else:
            cash.append("Ошибка! На вход подано число " + str(n) + ", не удовлетворяющее условиям процесса Капрекара")
            break
    else:
        if cash[-1] not in [495, 6174, 549945, 631764]:
            cash.append("Следующее число - " + str(n) + ", кажется процесс зациклился...")
    for i in range(len(cash)):
        print(cash[i])

n = int(input())

kaprekar_loop(n)