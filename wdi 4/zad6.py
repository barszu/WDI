def sort_sc(tab1 , tab2):
    #dziala tylko wtedy kiedy 2 ciagi sa rosnace
    if len(tab2) > len(tab1) : tab1 , tab2 = tab2 , tab1
    l1 , l2 = len(tab1) , len(tab2)
    sorted_tab = [0]*(l1+l2)
    x = 0
    y = 0
    i = 0
    przepisz_tab1 , przepisz_tab2 = False , False
    while przepisz_tab1 == False and przepisz_tab2 == False :
        a = tab1[x]
        b = tab2[y]
        
        if a == 0 : 
            przepisz_tab2 = True
            break
        elif b == 0 :
            przepisz_tab1 = True
            break
        
        if a < b :
            sorted_tab[i] = a
            x += 1
        elif a == b :
            sorted_tab[i] = a
            x += 1
            y += 1
        else:
            sorted_tab[i] = b
            y += 1
        
        if x > (l1-1) and y <= (l2-1) : przepisz_tab2 = True
        elif y > (l2-1) and x <= (l1-1) : przepisz_tab1 = True
        
        i += 1
    
    if przepisz_tab1: sorted_tab[i:] = tab1[x:]
    elif przepisz_tab2 : sorted_tab[i:] = tab2[y:]
    
    d_l = (l1 + l2) - len(sorted_tab)
    if d_l > 0 :
        sorted_tab = sorted_tab + [0]*d_l
    # elif d_l < 0 :
    #     sorted_tab = sorted_tab[:(l1+l2)]
    return sorted_tab


def zad6(tab2d):
    N = len(tab2d)
    M = N*N
    t2 = [0]*M
    
    a = tab2d[0]
    for i in range(1 , N):
        a = sort_sc(a , tab2d[i] )
    
    t2[:len(a)] = a
    return t2

print(zad6([[1,2,3,4] , [2,4,5,7] , [3,4,5,8],[1,2,3,5]]))
