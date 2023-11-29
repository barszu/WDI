def wyznacznik_zwykly(T):
    for i in range(3):
        T[i] = T[i]*2
    
    wynik = 0
    for k in range(3):
        wyr = 1
        for w in range(3):
            wyr *= T[k] [k]