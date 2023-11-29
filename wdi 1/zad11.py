from math import isqrt

def sum_d(number):
    sum_od_d = 0
    for d in range(1 , isqrt(number)+1):
        if number % d == 0 :
            sum_od_d += d
            sum_od_d += number//d
    return sum_od_d - number   
   
   
max_num = 10**6    
for no1 in range(max_num):
    no2 = sum_d(no1)
    if no2 > max_num: continue
    if sum_d(no2) == no1 :
        print(no1 , no2)
