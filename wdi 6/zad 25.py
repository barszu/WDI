def is_prime(a):
    from math import isqrt
    for d in range(2 , isqrt(a)+1):
        if a%d == 0 : return False
    return True

def droga(poz, T:list, kroki:list):
    i = 2
    while i < len(T) - poz :
        if T[poz]%i == 0 and is_prime(i) :
            if kroki[poz+i] != -1 :
                kroki[poz+i] = kroki[poz] + 1
                droga(poz+i , T , kroki)

def szukaj(T):
    N = len(T)
    kroki = [-1 for i in range(N)]
    kroki[0] = 0
    droga(0 , T , kroki)
    return kroki[N-1]

"ITERACYJNIE"
def iter(T):
    n = len(T)
    from math import inf
    T1 = [inf]*n
    T[0] = 0
    for i in range(n):
        if (T1[i] != inf):
            k = 2
            z = T[i]
            from math import isqrt
            while(z>1 and k<isqrt(2)+1):
                if (z%k == 0):
                    if(i+k>= n): break
                while(z%k == 0): z/= k
                T[i+k] = min(T[i+k] , T[i] +1 )
            if (z>1 and i+z < n) : T[i+2] = min(T[i+2] , T[i] + 1)
    return T[n-1]