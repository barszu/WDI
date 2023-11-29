def f(T, w , k):
    if w == 7 : return T[w][k]
    
    from math import inf
    
    if k > 0 : left = f(T,w+1 , k-1)
    else: left = inf
    
    if k < 7 : right = f(T,w+1,k+1)
    else: right = inf
    
    middle = f(T , w+1 , k)
    
    return min(left, middle , right) + T[w][k]

import random as r
T = [[r.randint(1,9) for _ in range(8)] for __ in range(8)]
print(T)
print(f(T,0,5))