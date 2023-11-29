def d_assmb_num(num):
    from math import isqrt
    str_tab =''
    condition = True
    while condition :
        b = isqrt(num) + 1
        for d in range(2 , b + 1):
            if num % d == 0:
                str_tab += (str(d) + "-")
                num = num//d
                break
            elif b == d :
                condition = False
                #num jest juz liczba pierwsza
    if num > 1 :
        str_tab += str(num)
    tab = [ int(y) for y in str_tab if y != "-" ]
    return tab

def zbior(lista):
    zbior = []
    for i in lista:
        if i not in zbior :
            zbior.append(i)
    return zbior

def zad8(tab):
    # tab = [ 2 , 5 , 6 , 33 , 4 , 5 , 99 , 66 , 75 , 45 ]
    l = len(tab)
    maska = [False]*l
    maska[0] = True
    for i in range(l):
        if maska[i]:
            for x in zbior(d_assmb_num(tab[i])):
                new_id = x + i
                if new_id < l :
                    maska[new_id] = True
                else: break
        if maska[-1] : return maska[-1]
    return maska[-1]

print(zad8([ 1 , 5 , 6 , 33 , 4 , 5 , 99 , 66 , 75 , 45 ]))