def zad1(N = 5):
    t = [[0 for _ in range(N)] for _ in range(N) ]
    kierunki = [(0,1),(1,0),(0,-1),(-1,0)] # prawo , dol , lewo , gora
    num = 1
    cond = True
    uzywane_N = N
    
    for i in range(N):
        t[0][i] = num
        num += 1
    
    kierunek_bierz = 1
    ost_wiersz = 0
    ost_kolumna = None
    
    while cond :
        kierunek = kierunki[kierunek_bierz]
        x_kier , y_kier = kierunek[1] , kierunek[0]
        if x_kier != 0 and y_kier == 0 :
            if x_kier == 1 :
                
            elif x_kier == -1 :
        
        
        
        
        if kierunek_bierz == 4 : kierunek_bierz = 0
        num += 1