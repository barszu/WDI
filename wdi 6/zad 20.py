def zad19(w_start,k_start):
    # from random import randint
    # T = [ [0]*8 for _ in range(8) ]
    # for x in range(8):
    #     for y in range(8):
    #         T[x] [y] = randint(10,99)
    # for _ in range(8): print(T[_])
    T = [[43, 93, 34, 57, 90, 23, 81, 57],[84, 18, 48, 45, 24, 34, 95, 31],[15, 43, 92, 41, 35, 97, 60, 24],[47, 83, 49, 11, 34, 77, 14, 76],[86, 61, 25, 99, 84, 77, 85, 73],[92, 45, 65, 69, 72, 80, 69, 99],[51, 37, 31, 62, 11, 88, 62, 80],[29, 86, 80, 19, 59, 70, 42, 58]]
    #---------------------------------------------
    def ending(num): #koncowka liczby cyfra
        return num%10

    def begin(num): #poczatek liczy cyfra
        from math import log10
        # n = int(log10(num))
        n = len(str(num)) - 1
        return num//(10**n)


    def canIfn(w,k,old_ending:int):
        nonlocal T
        if 0 <= w < 8 and 0 <= k < 8 :
            #jestesmy w planszy przy tym ruchu
            if not already_visited[w] [k]: 
                new_begin = begin(T[w] [k])
                if old_ending < new_begin : return True
                else: return False
        else: return False
        
    already_visited = [ [False]*8 for _ in range (8)]
    dobra_droga = []

    def rek(w,k,droga=[],canI_be_here=True): 
        nonlocal already_visited , T , dobra_droga
        # z tresci wynika ze krol stoi na polu o indeksie [0][0] i moze sie poruszac tylko w dol w prawo i po przekatnej (w prawy dolny rog)
        # canI_be_here - true / false -> czy moze byc na tym polu -> uruchamia sie sprawdzenie
        if not canI_be_here: return False
        if (w,k) in [(0,0), (7,7), (0,7), (7,0)] : 
            dobra_droga = droga
            return True
        
        end = ending(T[w] [k])
        already_visited[w] [k] = True
        
        for (dw,dk,kierunek) in [(0,1,0),(1,-1,1),(0,-1,2),(-1,-1,3),(-1,0,4),(-1,1,5),(0,1,6),(1,1,7)]: #załaczony backtracing
            if rek(w+dw , k+dk , droga+[kierunek], canIfn(w+dw , k+dk , end)) : return True
        return False
    
    return rek(w_start , k_start) , dobra_droga

print(zad19(3,7))