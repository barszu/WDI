def sr_geoart( a , b , E = 0.0001):
    from math import sqrt
    while abs(a-b) > E:
        a , b = (a+b)/2 , sqrt(a*b)
    return a

print(sr_geoart(24 , 6))