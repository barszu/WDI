def sr_m(T):
    sum_x = 0
    sum_y = 0
    n = len(T) 
    for pkt in T:
        sum_x += pkt[0]
        sum_y += pkt[1]
    
    return (sum_x/n , sum_y/n)

def odleglosc(pkt):
    x = pkt[0]
    y = pkt[1]
    from math import sqrt
    return sqrt((x**2) + (y**2))

def rek(t,r,k,i,A):
    if i==len(t):
        n = len(A)
        if n == 0 or n > k or (n%3 != 0): return False
        # liczy srodek masy i sprawdza go
        return odleglosc(sr_m(A)) < r

    return rek(t,r,k,i+1,A+[ t[i] ]) or rek(t,r,k,i+1,A)