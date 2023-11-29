def zad11(T,num):
    n = len(T)
    wynik = []
    
    def rek_en(i ,temp_iloczyn = 1 ,ilosc = 0):
        nonlocal n
        nonlocal num
        nonlocal T
        nonlocal wynik
        
        if i == n :
            if temp_iloczyn == num : 
                wynik += [ilosc]
            return False

        return rek_en(i+1 , temp_iloczyn*T[i], ilosc+1) or rek_en(i+1 , temp_iloczyn , ilosc)
    
    rek_en(0) #start
    return len(wynik)

print(zad11([2,55,66,77,10,6,20,3] , 60))
