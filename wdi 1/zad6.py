# x^x - 2020 = 0
x = 0
d = 0.001

def fx(x):
    return (x**x)

#szukanie domkniecia b
while True:  
    wynik = x**x
    if wynik > 2020 : break
    x += 1
b = x
a = 0

while abs(b - a) > d :
    sr = (a + b) / 2
    if fx(a)*fx(sr) < 0 :
        b = sr
    elif fx(b)*fx(sr) < 0 :
        a = sr
    else:
        for el in [sr , a , b] :
            if fx(el) == 0 :
                print(el)
                break
else:
    print(a , a**a)