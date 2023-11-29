# (x1 , x2 , y1 , y2)

def pole(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)

def nachodzenie(p1 , p2):
    # chce aby p1 bylo pietrwsze a p2 dopasowywane czyli p1_x1 <p2_x1
    if p1[0] > p2[0]: p1 , p2 = p2, p1
    if (p1[0] <= p2[0] <= p1[1]) or (p1[0] <= p2[1] <= p1[1]): return False
    # if (p1[2] <= p2[2] <= p1[3]) or (p1[2] <= p2[3] <= p1[3]): return False
    return True

def check(T):
    n = len(T)
    for i in range(n-2):
        for j in range(i+1 , n-1):
            if not nachodzenie( T[i] , T[j] ) : return False
    return True


#rekurencyjnie wybieram podzbiory o dlugosci 13 takie ze suma pol = 2022

def zad27(T,sum_dana):
    
    def rek(T,i=0 , r=sum_dana , temp_podz = []):
        if i == len(T) and len(temp_podz) < 13 : return False # warunek dojscia do konca i wykluczenia
        if len(temp_podz) == 13 :
            #koniec tej rekurencji jest 13 wybrane
            if not r == 0 : return False
            return check(temp_podz)
            
        return rek(T,i+1 ,r-pole(*T[i]), temp_podz + [T[i]]) or rek(T,i+1 , temp_podz)

