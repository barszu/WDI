def long_float( a , d , n):
    wynik = str(a//d)
    
    if n == 0 : return wynik
    
    wynik += ","
    n_c = 1
    
    while (a != 0 and n_c <= n) :
        a = a%d * 10
        wynik += str(a//d)
        n_c += 1
    #end while
    
    return wynik
    
a = int(input("a >>> "))
d = int(input("b >>> "))
n = int(input("n >>>"))

print(long_float(10 , 3 , 50))