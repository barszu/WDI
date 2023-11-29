def is_prime(a):
    from math import isqrt
    for d in range(2 , isqrt(a)+1):
        if a%d == 0 : return False
    return True

def dekoder(T:list): #10101 l = 5 
    l = len(T)
    wynik = 0
    mnoznik = 1
    for i in range(l -1 , -1 , -1):
        wynik += mnoznik*T[i]
        mnoznik *= 2
    return wynik

def foo(T, ix , begin ):
    liczba_b = T[begin:ix]
    liczba = dekoder(liczba_b)
    if is_prime(liczba):
        if ix == len(T)-1 : return True
        return foo(T,ix+2,ix+1) or foo(T,ix+1,begin)
    else: 
        if ix == len(T)-1 : return False
        return foo(T,ix+1,begin)


def rek(T):
    N = len(T)
    if T[N-1]==0 : return False
    return foo( T, 1 , 0)

print(rek([1,1,1,0,1,1]))
