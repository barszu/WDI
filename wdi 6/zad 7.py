def f(T,n,i,r):
    if r == 0 : return True
    if r<0 or i > n-1 : return False
    return f(T,n,i+1,r) or f(T,n,i+1,r-T[i]) 
        #   nie biore        biore

def zad7(T,M):
    n = len(T)
    return f(T,n,0,M)

print(zad7([6,2,4] , 13))