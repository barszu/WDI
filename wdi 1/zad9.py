def d_list(number):
    from math import isqrt
    d_list = [ 1 , number ]
    for d in range(2 , isqrt(number)+1):
        if number % d == 0 :
            d_list.append( d )
            d_list.append(int(number/d))
    return sorted(d_list)

print(d_list(947_156_569_998))