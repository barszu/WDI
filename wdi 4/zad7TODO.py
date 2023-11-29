[
    [4 , 7 , 8]  juz posortowane
    [1 , 3 , 6]  juz posortowane
    [4 , 4 , 8]  juz posortowane
]
==> wynikowa dlugosc 3^2 = 9
[ 1 , 3 , 4 , 4 , 4 , 6 , 7 , 8 , 8]

#zobacz sortowanie przez wstawianie <- wlasciwe sortowanie
#IDEA scal tablice wielowymiarowa w jedna i sortuj bombelkowo
def zad7(tab1):
    n = len(tab1)
    tab = [0]*(n**2)
    # True - nie wykorzystany element
    tab_masek = [[True]*n]*n
    tab_ids = [i for i in range(n)]
    
    
    min = tab1[0][0]
    for i1 in tab_ids :
        for i2 in tab_ids:
            