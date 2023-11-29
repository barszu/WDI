def joinlist(*arg):
    str_ = ""
    for i in arg:
        str_ += str(i)
    return str_

def dz(a , b , N = 20 , asstr = False):
    w = [a//b]
    #0 el to int z dzielenia reszta czesc po przecinku
    a = (a%b) * 10
    for _ in range(N):
        w.append(a//b)
        a = (a%b) * 10
    if asstr :
        return (str(w[0]) + "," + joinlist(*w[1:]))
    return w

def dod_tab_ulam(t1 , t2):
    # z przodu na id 0 jest czesc calkowita
    t2 = t2[::-1]
    t1 = t1[::-1]
    # t1 jest tablica dluzsza z zalozenia
    if len(t2) > len(t1): t1 , t2 = t2 , t1
    #naprawienie dlugosci tablicy krotszej -t2
    t2 = [0]*(len(t1)-len(t2)) + t2
    #tablica wynikowa w ktora sa wpisywane dane jest defultowo przekrecona
    tw = [0]*len(t1)
    
    for i in range(len(t1)-1):
        el = t1[i] + t2[i]
        if el >= 10 :
            tw[i] += el%10
            tw[i+1] += el//10
        else: tw[i] += el
    #dodanie czesci calkowitych
    tw[-1] += (t1[-1] + t2[-1])
    return tw[::-1]

def zad4(N , dok = 4 , dok2 = -1 ):
    e = [2] + [0]*N
    silnia = 1
    i = 2
    dok = (-1)*dok # jaka jest roznica miedzy e a kolejnym elememtrm
    #ktore elemty od konca identyczne
    zeras = [0]*N
    while True :
        silnia *= i
        el = dz(1 , silnia , N)
        b = el[:-1]
        if b == zeras :
            return (str(e[0]) + "," + joinlist(*e[1:]))
        
        # if i > 5 : 
        #     #sprawdzenie koncowek liczby e i tej wynikowej
        #     e_k = joinlist(*e[dok:dok2])
        #     el_k = joinlist(*el[dok:dok2])
        #     if e_k == el_k : return (str(e[0]) + "," + joinlist(*e[1:]))
        i += 1
        e = dod_tab_ulam(e , el)

print(zad4(10))
