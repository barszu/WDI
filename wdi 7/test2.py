#mamy szachownice n x n skoczki (input binary tab dim 2) nie wszystko szachowane, wstawic skoczka tak zeby zwioekszyc szachowane pola,
# puste pole polozone najblizej srodka szachownicy
# zakladamy ze dl boku nieparzysta >2

def skoczek(T,poz): #-> szachuje pola (Flase -nieszachowane , True-szachowane)
    n = len(T)
    moves = [(1,-2),(1,2),(2,-1),(2,1),(-1,-2),(-1,2),(-2,-1),(-2,1)]
    i = 0
    while True:
        
    
def place(T):
    n = len(T)

