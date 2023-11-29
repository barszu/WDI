def zad2(tab):
    N = len(tab)
    warunki = [False]*N
    tab_parz = [str(i) for i in range(0 , 9 , 2)]
    for idwiersza in range(N):
        
        for liczba in tab[idwiersza] :
            ma_tylko_cyfry_nieparzyste = True
            
            for cyfra in str(liczba) :
                if cyfra in tab_parz : 
                    ma_tylko_cyfry_nieparzyste = False
                    break
            if ma_tylko_cyfry_nieparzyste : warunki[idwiersza] = True
        
    return ([True]*N == warunki)

print(zad2([[17,3,2],[1,8,10],[2,16,20]]))