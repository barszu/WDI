def rozloz_na_czynniki(a , czynniki = [] ):
    if a == 1 : return czynniki
    from math import isqrt
    for d in range(2 , isqrt(a)+1):
        if a%d == 0 : 
            if d not in czynniki :
                czynniki.append(d)
            return rozloz_na_czynniki(a//d , czynniki )
            
    else: 
        if a not in czynniki: 
            czynniki.append(a)
    return czynniki


    
    

def main(T):
    n = len(T)
    waga = [0]*n
    for i in range(n):
        waga[i] = len(rozloz_na_czynniki(T[i]))
    
    def sum(T):
        c = 0
        for i in range(len(T)):
            c += T[i]
        return c
    
    
    def rek(T , i , A = [] , B = [], C = []):
        if i == len(T):
            if len(A) > 0 and len(B) > 0 and len(C) > 0 :
                if sum(A) == sum(B) == sum(C): 
                    return True 
            return False
        
        return rek(T, i+1 , A+[T[i]] , B , C) or rek(T, i+1 , A , B+[T[i]] , C) or rek(T, i+1 , A , B , C+[T[i]])
    
    return rek(waga,0)

tab = [1,2,6,30,15]
# debuguj 
print(main(tab))