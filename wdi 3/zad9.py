def zad9(tab):
    l = len(tab)
    podciag = 1
    podciag_max = 1
    for i in range( 1 , l ):
        k = tab[i] - tab[i-1] #chwilowe r
        if k > 0 : podciag += 1
        else:
            podciag = 1
        if podciag > podciag_max : podciag_max = podciag
    return podciag_max


print(zad9([2 , 1 , -1 , -2 , 1 , 2 , 3 , 4 , 5 , 7 , 9 , 10 , 0 , 5 , 1 , 2]))