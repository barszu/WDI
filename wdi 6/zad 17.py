# a , b -> c (wszystkie cyfry zachowane, kolejnosc zachowana , )
# ile liczb pierwszych mozna zbudowac

def int_to_tab(int_):
    from math import log10
    n = int(log10(int_))+1
    T = [0]*n
    def engine(num,i=0):
        T[i] = num%10
        return engine(num//10 , i+1)
    return T[::-1]

def is_prime(num):
    for d in range(2 , int(num**0.5)+1 ):
        if num%d == 0 : return False
    return True

def zad(a,b):
    a = str(a)
    b = str(b)
    la = len(a)
    lb = len(b)
    c = 0
    L = la + lb
    
    def rek(wyraz='' , i=0 , j=0): #-> main c , extras +c
        nonlocal c , la , lb , a , b , L
        
        if lb > j and la > i:
            # ... generuj wyrazy a b
            #biore z A / biore z B
            return rek(wyraz+a[i], i+1 , j) or rek(wyraz+b[j] , i , j+1)
        
        elif lb == j and la > i :
            # ... doklej reszte z a
            return rek(wyraz+a[i:] , la , lb)
            
        elif lb > j and la == i :
            # ... doklej reszte z b
            return rek(wyraz+b[j:] , la , lb)
            
        elif lb == j and la == i :
            if is_prime(int(wyraz)): c += 1
            return False
    
    rek()
    return c

print(zad(19,19))