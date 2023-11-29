import random
def zad6(N):
    #tworzenie tablicy
    tab = [None]*N
    for i in range(N):
        tab[i] = random.randint(1 , 1000)
    #sprawdzanie czy kazda z liczb ma cyfre jakas nieparzysta
    cond = True
    for el in tab:
        if cond == False : break
        tem_cond = False
        for x in str(el):
            if int(x)%2 != 0 : 
                tem_cond = True
                break
        if tem_cond == False : cond = False
    return tab , cond

print(zad6(2))
