# S id = S wart
def zad6(T):
    n = len(T)
    # T_id = [i for i in range(n)]
    from math import inf
    tab_podz = (inf , 0) #dlugosc_ciagu , suma_wewnetrzna
    
    def rek(T , i , suma_el = 0 , suma_id = 0 , dl = 0): 
        nonlocal tab_podz 
        
        if i == len(T):
            if dl > 0 :
                # sprawdz waruenk z zadnia ze 
                if suma_el == suma_id :
                    if dl <= tab_podz[0] and suma_el > tab_podz[1] :
                        tab_podz = (dl , suma_el)
            return False
        
        return rek( T, i+1 , suma_el+T[i] , suma_id + i , dl+1) or rek(T, i+1 , suma_el , suma_id , dl )
                    #              biore el                                  nie biore el
    #engine start
    rek(T,0)
    
    
    return tab_podz

print(zad6([1,7,3,5,11,2]))