def to_sys(num , base):
    #zbior danych podstaw
    znaki = [str(x) for x in range(0 , 9 +1)] + [chr(y) for y in range(ord("A") , ord("F") + 1)]
    w = ""
    while num > 0 :
        w += znaki[num%base]
        num //= base
    return w[::-1]

def zad1(num):
    for base in range(2 , 16 + 1):
        print(to_sys(num , base) , base)

zad1(58)