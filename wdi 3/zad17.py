def mask_gen(lenth , b):
    
    def bins(num , lenth , b):
        #returns binary representation with 0 in front of to fullfill
        bins = ""
        while num != 0:
            bins += str( num%b )
            num = num//b
            
        bins = bins[::-1]
        while len(bins) < lenth :
            bins = "0" + bins
        return bins
    
    mask_list = [bins(i , lenth , b) for i in range(b**(lenth))]
    return mask_list

def zlicz(tab , el):
    c = 0
    for i in tab:
        if i == el : c += 1
    return c

def is_prime(a):
    is_prime = True
    from math import isqrt
    for d in range(2 , isqrt(a)+1 ):
        if a%d == 0 :
            is_prime = False
            break
    return is_prime

def zad17(tab1 , tab2):
    l = len(tab1)
        #0 - bierz z obu
        #1 - bierz z 1
        #2 - bierz z 2
    c = 0
    for mask in mask_gen( l , 3 ):
        suma = 0
        #dekoder
        id = 0
        for m in mask:
            if m == "0" : suma += (tab1[id] + tab2[id])
            elif m == "1" : suma += tab1[id]
            elif m == "2" : suma += tab2[id]
            id += 1
        #sprawdzenie czy suma jest liczba pierwsza
        if is_prime(suma) and suma > 2: 
            print(suma)
            c += 1
    print(float(c))

zad17([1,3,2,4] , [9,7,4,8])