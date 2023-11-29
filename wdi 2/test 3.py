def is_prime(num):
    if num%2 == 0 or num%3 == 0 : 
        return False
    from math import isqrt
    #dla duzych liczb
    if num > 100:
        k = 1
        while (6*k - 1 < isqrt(num) + 1):
            if num%(6*k - 1) == 0 or num%(6*k + 1) == 0 :
                return False
            k += 1
        else: return True
    #dla mniejszych liczb
    else:
        for d in range(2 , isqrt(num) + 1):
            if num%d == 0 : return False
        else: return True


print(is_prime(75123))