def is_prime(a):
    from math import isqrt
    for d in range(2 , isqrt(a)+1):
        if a%d == 0 : return False
    return True

def zad2(N):
    starting_primes = [2 ,3]
    if N <= 2 : return None # n = 2 n =1 , n = 0
    for i in starting_primes:
        if i < N : print(i)
    if N > 6 :
        k = 1
        while 6*k - 1 < N :
            liczby = [6*k - 1 , 6*k + 1] # 5 , 7
            if is_prime(liczby[0]) and liczby[0] < N : print(liczby[0])
            if is_prime(liczby[1]) and liczby[1] < N : print(liczby[1])
            k += 1
            
zad2(10**12)