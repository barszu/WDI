# from random import randint
# T = [ [0]*8 for _ in range(8) ]
# for x in range(8):
#     for y in range(8):
#         T[x] [y] = randint(10,99)
# for _ in range(8): print(T[_])
T = [[43, 93, 34, 57, 90, 23, 81, 57],[84, 18, 48, 45, 24, 34, 95, 31],[15, 43, 92, 41, 35, 97, 60, 24],[47, 83, 49, 11, 34, 77, 14, 76],[86, 61, 25, 99, 84, 77, 85, 73],[92, 45, 65, 69, 72, 80, 69, 99],[51, 37, 31, 62, 11, 88, 62, 80],[29, 86, 80, 19, 59, 70, 42, 58]]
#---------------------------------------------

def nadpisz_tab(w,k,moge_byc):
    moge_byc[w] = [False]*8
    for i in range(8):
        moge_byc[i] [k] = False
    return moge_byc

def rek(T , w , k , suma , moge_tu_byc): #-> bool #moge tu byc tabloica booli czy moge sie wznajdowac na pozycji x,y
    # - tworzy podzbior wybiera el zapisuje ich sume 
    
    #naprawienie wyjscia poza tablice
    if k == 8: k , w = 0 , w+1
    if w == 8 : return False # KONIEC REKURENCJI NIE MAM KROKOW
    
    #czy moge tu byc?
    if not moge_tu_byc[w] [k] : 
        #nie biore
        return rek(T,w,k+1,suma,moge_tu_byc)
    
    if suma == 0 : return True
    elif suma < 0 : return False
    #                               biore                            /               nie biore
    return rek(T , w , k+1 , suma-(T[w] [k]) , nadpisz_tab(w,k,moge_tu_byc)) or rek(T ,w ,k+1,suma,moge_tu_byc)
    



def zad21(zadana_suma,T): #-> TRUE FALSE
    #el postawiony skresla kolumne i wiersz
    moge_tu_byc = [ [True]*8 for _ in range(8)]
    return rek(T,0,0,zadana_suma,moge_tu_byc)

print(zad21(61 , T))
