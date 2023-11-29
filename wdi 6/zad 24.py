# xsr = art(x)
    # stworz podzbior -> srodek ciezkosci policz , 
    # zapisuj dopelnienie -> wygeneruj podzbior z tego -> srodek ciezkosci policz porownaj
    # policz odleglosc miedzy tymi srodkami masy
    #GLOBAL najmniejsza odlegosc = min(zapisana , bierzaca)

def zad24(T):
    n = len(T)
    from math import inf
    naj_odleg = inf
    
    def sr_masy(T):
        c = len(T)
        sum_x = 0
        sum_y = 0
        for (x,y) in T :
            sum_x += x
            sum_y += y
        return (sum_x/c , sum_y/c)
    
    def odleglosc_pkt(pkt1 , pkt2):
        D_x = abs(pkt1[0] - pkt2[0])
        D_y = abs(pkt1[1] - pkt2[1])
        from math import sqrt
        return sqrt( (D_x**2) + (D_y**2) )
    
    def gen_podz1(i=0,A=[],B=[]):
        nonlocal T , n
        if i == n : 
            if len(A)==0 or len(B)==0: return
            #mamy ciag A i uzupelnienie B
            #oblicz punkt srodka masy
            sA = sr_masy(A)
            return gen_podz2(B,sA)
            
            #biore / nie biore
        return gen_podz1(i+1,A+[ T[i] ],B) or gen_podz1(i+1,A,B+[ T[i] ])
    
        
    def gen_podz2(B,sA,i=0,C=[]):
        nonlocal naj_odleg
        if i == len(B): #koniec
            if len(C)==0 : return
            sC = sr_masy(C)
            naj_odleg = min(naj_odleg , odleglosc_pkt(sA , sC))
            return naj_odleg
        
        #biore nie biore
        return gen_podz2(B,sA,i+1,C+[ B[i]]) or gen_podz2(B,sA,i+1,C)
    
    gen_podz1()
    return naj_odleg

print(zad24([(1.5 , 5.7),(6.8 , 9.0),(5.4 , 1.0) ]))
