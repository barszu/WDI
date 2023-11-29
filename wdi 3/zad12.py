def tab_gen(N):
    import random
    tab_of_num = [p for p in range(1 , 100 , 2)]
    l = len(tab_of_num)
    tab_N = [0]*N
    for id in range(N):
        tab_N[id] = tab_of_num[random.randint(0 , l-1)]
    return tab_N

def zad12(N , tab = []):
    if tab == [] : 
        tab = tab_gen(N)
        print(tab)
    else: N = len(tab)
    
    max_ros , max_mal = 1 , 1 #max dlugosc rosnacego , malejacego
    r_old = tab[1]-tab[0]  #ogolne stare porownywane bedzie z temp
    x  = 0
    for y in range(1 , N):
        r = tab[y] - tab[y-1]
        sp_ending_con = ((y == N - 1) and (r == r_old))
        if r != r_old or sp_ending_con :
            l = y - x 
            if sp_ending_con : l += 1
            
            if r_old > 0 : max_ros = max(max_ros , l)
            elif r_old < 0 : max_mal = max(max_mal , l)
            x = y - 1
            r_old = r
    #po iteracjach tu r_old jest  jako r
    if (tab[-1] - tab[-2]) != (tab[-2] - tab[-3]) :
        l = 2
        if r > 0 : max_ros = max(max_ros , l)
        elif r < 0 : max_mal = max(max_mal , l)
    return max_ros , max_mal

            
    
print(zad12(1 , [1,2,3,1]))