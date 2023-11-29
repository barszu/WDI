def ilosc_1(T):
    c = 0
    for num in T :
        while num != 0:
            if num%2 == 1: c+=1
            num = num//2
    return c



def rek1(T,i=0,A=[],B=[],C=[]):
    if i == len(T): 
        if len(A) == 0 or len(B) == 0 or len(C) == 0 : return False
        a1 = ilosc_1(A)
        b1 = ilosc_1(B)
        c1 = ilosc_1(C)
        return ( (a1==b1) and (b1==c1) )
    
    #do wora A B C albo nigdzie
    return rek1(T, i+1 , A+[ T[i] ] , B , C) or rek1(T, i+1 , A , B +[ T[i] ] , C) or rek1(T, i+1 , A , B , C+[ T[i] ] ) or rek1(T, i+1 , A , B , C )

print(rek1([1,3,4,5,6,6,5,3,2,1,3,4,5,6,67,7]))