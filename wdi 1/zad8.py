def is_prime(number):
    from math import isqrt
    is_prime = True
    for d in range(2 , isqrt(number)):
        if number%d == 0 :
            is_prime = False
    return is_prime

print(is_prime(31))