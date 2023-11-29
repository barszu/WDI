def zad10(tab):
    l = len(tab)
    podciag = 1
    podciag_max = 1
    r = tab[1] - tab[0]
    for i in range( 1 , l ):
        k = tab[i] - tab[i-1] #chwilowe r
        if k == r : podciag += 1
        else:
            r = k
            podciag = 2
        if podciag > podciag_max : podciag_max = podciag
    return podciag_max