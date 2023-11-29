def pierw( num , n = 2 , E = 0.00001) :
    x = 1
    while True:
        old_x = x
        x = (1/n) * (((n-1) *x) + (num/(x**(n-1))))
        if abs(old_x - x) < E :
            break
    return x

print(pierw(69 , 4))
