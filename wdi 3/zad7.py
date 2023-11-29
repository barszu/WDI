def zad7(N):
    import random
    #tworzenie tablicy
    tab = [None]*N
    for i in range(N):
        tab[i] = random.randint(1 , 1000)
    #sprawdzanie czy kazda z liczb ma cyfre jakas nieparzysta
    cond = True
    for el in tab:
        if cond == False : break
        for x in str(el):
            if int(x)%2 == 0 : 
                cond = False
                break
    return tab , cond

print(zad7(1))