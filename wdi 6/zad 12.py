def zad11(T,num):
    n = len(T)
    wynik = []
    
    def rek_en(i ,temp_iloczyn = 1 ,ilosc = 0, wyrazy = []):
        nonlocal n , num , T , wynik
        if temp_iloczyn > num: return False
        
        if i == n :
            if temp_iloczyn == num : 
                wynik += [wyrazy]
            return False

        return rek_en(i+1 , temp_iloczyn*T[i], ilosc+1 , wyrazy+[ T[i] ]) or rek_en(i+1 , temp_iloczyn , ilosc, wyrazy)
    
    rek_en(0) #start
    return wynik

print(zad11([2,55,66,77,10,6,20,3] , 60))