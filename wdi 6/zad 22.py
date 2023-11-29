def czynniki(num):
    T =[]
    
    def rek(num):
        nonlocal T
        from math import isqrt
        
        for d in (2 , isqrt(num)+1):
            if num%d == 0 : 
                if d not in T : T+=[d]
                return rek(num//d)
        if num > 1 : 
            T+=[num] 
            return
    
    rek(num)
    
    return T

def zad(T):
    
    def rek(i=0 , skok=0):
        nonlocal T 
        if i == len(T)-1 : return skok
        if i >= len(T) : return -1
        
        #wywolaj sie (skakaj) nie wiadomo ile razy?
        for k in czynniki(T[i]) :
            return rek(i+k , skok+1)
        
        return -1
    
    return rek()

print(zad([2,2,1,4,5,6,7,8]))