#gliczuje sie i nie dziala
def f(T,n,i,r):
    if r == 0 : return True
    if r<0 or i > n-1 : return False
    return f(T,n,i+1,r) or f(T,n,i+1,r-T[i]) or f(T,n,i+1,r+T[i])
        #   nie biore        biore              #na druga szalke

def zad8(T,M):
    n = len(T)
    T.sort()
    return f(T,n,0,M)

print(zad8([6,1,10] , 5))

