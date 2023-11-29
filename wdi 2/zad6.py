from math import isqrt
num = int(input(">>>"))
for d in range(int((num**0.5)) , 1  , -1 ):
    if num%d == 0:
        print( num , d , num//d)
        break