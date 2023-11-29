def zad2(tab):
    N = len(tab)
    tab_parz = [str(i) for i in range(0 , 9 , 2)]
    
    for wiersz in tab:
        warunki = [False]*N
        idcyfry = 0
        for liczba in wiersz :
            ma_chociaz_jedna_cyfr_parz = False
            
            for cyfra in str(liczba) :
                if cyfra in tab_parz : 
                    ma_chociaz_jedna_cyfr_parz = True
                    break
            
            if ma_chociaz_jedna_cyfr_parz : warunki[idcyfry] = True
            idcyfry += 1
        
        if [True]*N == warunki : return True
    
    return False

print(zad2([[17,3,5],[1,8,11],[2,16,11]]))