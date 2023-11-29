#podzbiory nie sa rozlaczne zakladam
def rek(T,k,i=0,A=[]):
    if len(T) == i :
        suma_elA = sum(A)
        k = k - len(A)
        if k < 0 : return False
        return rek2(T,k,A,suma_elA)
    
    return rek(T,k,i+1,A+ [ T[i] ]) or rek(T,k,i+1,A)

def rek2(T , k , A , suma_elA , i=0 , B=[]): #k zmniejszam z kazdym dodaniem el
    if k < 0 or (len(T) == i and k > 0): return False
    if k == 0 :
        if B == A : return False
        suma_elB = sum(B)
        return suma_elB == suma_elA #bool
    
    return rek2(T , k-1 , A , suma_elA , i+1 , B+[ T[i] ]) or rek2(T , k , A , suma_elA , i+1 , B)

print(rek([1,2,5,7,9] , 3))
    