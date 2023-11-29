def zad4(tab2):
    N = len(tab2)
    
    tab_sum_el_w_kolumnie = [0]*N
    for i in range(N):
        # i reprezentuje id kolumny
        sum_el_w_kolumnie = 0
        for y_el in range(N):
            sum_el_w_kolumnie += tab2[y_el][i]
            
        tab_sum_el_w_kolumnie[i] = sum_el_w_kolumnie
    
    odp = [0,0,0] #maxy dla | sum_k/sum_w czyli p | , x , y
    for y in range(N):
        
        sum_el_w_wierszu = 0
        for x_el in tab2[y]:
            sum_el_w_wierszu += x_el
        
        for x in range(N):
            # tutaj dane juz jest x i y (kordy el)
            p = tab_sum_el_w_kolumnie[x]/sum_el_w_wierszu
            if p > odp[0] :
                odp = [p,x,y]
    return odp

print(zad4([[1,4,26],[1,3,-1000],[1,8,200]]))
