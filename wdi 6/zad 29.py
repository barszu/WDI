def sr_m(T):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    n = len(T) 
    for pkt in T:
        sum_x += pkt[0]
        sum_y += pkt[1]
        sum_z += pkt[2]
    
    return (sum_x/n , sum_y/n , sum_z/n)

def odleglosc(pkt):
    x = pkt[0]
    y = pkt[1]
    z = pkt[2]
    from math import sqrt
    return sqrt((x**2) + (y**2) + (z**2))



def rek1(T,r,A,i):
    if i == len(T):
        if len(A) < 3 : return False
        #mamy podzbior
        #wylicz srodek masy
        sr_masy = sr_m(A)
        #sprawdz odleglosc jego
        d = odleglosc(sr_masy)
        return (d < r)
        
    
    return rek1(T,r,A + [ T[i] ] , i+1) or rek1(T,r,A,i+1) #biore nie biore