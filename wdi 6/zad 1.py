# 451 151 555 466
# <a , b)

def is_prime(a):
    from math import isqrt
    for d in range(2 , isqrt(a)+1):
        if a%d == 0 : return False
    return True

def num_out(a , i):
    from math import log10
    l = int(log10(a)) + 1
    front_cut = 10**(l-i)
    przod_liczby = (a//front_cut)*(front_cut//10)
    back_cut = 10**(l-1-i)
    tyl_liczby = a%back_cut
    return przod_liczby + tyl_liczby
    


def f(c:int , i = 0 , counter = 0 ):
    from math import log10
    l = int(log10(c)) + 1
    
    if i == l : #i max = len - 1
        return counter
    num_new = num_out(c , i)
    if l-1 >= 2 :
        if is_prime(num_new) == True : 
            counter += 1
        
    return f(c , i+1 , counter) #recursion

print(f(127))