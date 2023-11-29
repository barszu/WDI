def d_list(number):
    from math import isqrt
    d_set = set([ 1 , number ])
    for d in range(2 , isqrt(number)+1):
        if number % d == 0 :
            d_set.add( d )
            d_set.add(int(number/d))
    return sorted(list(d_set))

a = 12
b = 144
c = 24



def nwd(a , b , c):
    d_a = set(d_list(a))
    d_b = set(d_list(b))
    d_c = set(d_list(c))
    d_intersection = d_c.intersection(d_a.intersection(d_b))
    return max(d_intersection)

print(nwd(a ,b , c))