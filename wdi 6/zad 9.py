def zad8(T,M):
    n = len(T)
    T.sort()
    
    nlA = []
    nlB = []
    
    def f(T,n,i,r,A=[],B=[]): #A wlasciwa wazaca B odwaznik i inne
        nonlocal nlA , nlB
        
        if r == 0 :
            nlA = A
            nlB = B
            return True
        if r<0 or i > n-1 : return False
        return f(T,n,i+1,r,A,B) or f(T,n,i+1,r-T[i],A,B+[T[i]]) or f(T,n,i+1,r+T[i],A+[T[i]],B)
            #   nie biore        biore              #na druga szalke
    
    return (f(T,n,0,M) , nlA , nlB)


print(zad8([6,1,10] , 5))
