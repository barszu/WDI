def is_prime(num):
    is_prime = True
    from math import isqrt
    for d in range(2 , isqrt(num) + 1):
        if num % d == 0 :
            is_prime = False
            break
    return is_prime

def zad15(tab):
    N = len(tab)
    is_fib = [False]*N
    a , b = 0 , 1
    while a < N :
        is_fib[a] = True
        a , b = b , a+b
    
    prime_in_orf = False
    for id in range(N):
        if is_fib[id] :
            if tab[id] < 10 : return False
        else:
            if prime_in_orf == False :
                if is_prime : prime_in_orf = True
    return prime_in_orf

print(zad15([11,22,23,30,5]))