#generowanie cyfr z przedzialu 1 do 10**6
def suma_cyfr(num):
    suma_cyfr = 0
    for i in str(num):
        suma_cyfr += int(i)
    return suma_cyfr


for num in range(1 , 10**2):
    if num <= 3 :
        print(num)
    num_sum = suma_cyfr(num)
    #znajdywanie dzielnikow rozkladowych
    a = 85
    str_z_d = ""
    from math import isqrt
    while a > 1 :
        for d in range(2 , isqrt(a)):
            stare_a = a
            if a%d == 0:
                
                str_z_d += str(d)
                a = a//d
                break
        if stare_a == a : 
            str_z_d += str(a)
            break
    d_sum = suma_cyfr(str_z_d)
    if d_sum == num_sum : print(num)