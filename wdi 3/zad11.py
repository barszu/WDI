def zad11(tab):
    
    l = len(tab)
    podciag = 1
    podciag_max = 1
    q = tab[1] / tab[0]
    
    for i in range( 1 , l ):
        
        k = tab[i] / tab[i-1] #chwilowe r
        
        if k == r : podciag += 1
        # end if
        
        else:
            r = k
            podciag = 2
        # end else
        
        if podciag > podciag_max : 
            podciag_max = podciag
        # end if
        
    #end for        
    return podciag_max 
# end fun