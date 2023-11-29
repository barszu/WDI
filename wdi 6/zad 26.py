def is_prime(a):
    from math import isqrt
    for d in range (2,isqrt(a)+1):
        if a%d == 0 : return False
    return True

def zad26(A:int , B:int):
    if A <= 0 and B <= 0 : return 0
    n = A+B -1
    liczba = 2**n
    A -= 1
    wystapienia = 0
    
    def engine(liczba , A , B , krok ): # krok w sensie id od konca czyli 2 do potegi krok
        nonlocal n , wystapienia
        if krok == -1 or (A == 0 and B == 0): # warunek stopu cala lista jest juz przeiterowana
            #mam liczby w postaci 10
            if not is_prime(liczba): wystapienia += 1
            return False
        
        if A > 0 and B > 0 :
            return engine(2**krok + liczba , A-1 , B , krok-1) or engine(liczba, A , B-1 , krok-1 )# biore 1 / biore 0
        elif A == 0 and B > 0 : #mam do wyboru tylko 0 
            return engine(liczba, A , B-1 , krok-1 )
        elif B == 0 and A > 0 : #mam do wyboru juz tylko 1
            return engine(2**krok + liczba , A-1 , B , krok-1)
    
    
    engine(liczba , A , B , n-1)
    return wystapienia



print(zad26(2,3))