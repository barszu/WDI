# main - czy int wyjdzie z ktoregos ze wzorow
# 1. wybierz 3 (kombinacje)
# 2. zrob ich permutacje
# 3. dla permutacji sprawdz obcje 1 2 3 4

# glowna metodyka
# zad[bool] -> rek1[bool] -> rek2[bool] ->sprawdzenie obcji
def zad23(T):

    def A(R1,R2,R3): return float(R1+R2+R3)
    def B(R1,R2,R3): return float(R1) + 1/((1/R2) + (1/R3))
    def C(R1,R2,R3): return 1/((1/R1)+(1/R1*R2))
    def D(R1,R2,R3): return 1/((1/R1)+(1/R2)+(1/R3))

    def float_int(float_): return float_//1 == float_ 

    def rek1(T,n,i=0 , wyraz=[]): #-> [x,x,x]
        if len(wyraz) == 3 :
            # jest juz kombinacja
            return rek2(wyraz) #<- permutacje 
        if i == n : #poza tablica juz jestesmy
            return 
        #biore / nie biore
        return rek1(T,n,i+1 , wyraz + [ T[i] ] ) or rek1(T,n,i+1 , wyraz)

    def rek2(t , wyraz=[] , uzyte=[False,False,False]) : #- permutacje 
        if len(wyraz) == 3 : 
            return sprawdz_obc(wyraz)
        for i in range(len(t)):
            if not uzyte[i] :
                uzyte[i] = True
                return rek2(t , wyraz+[ t[i] ] , uzyte )

    def sprawdz_obc(wyraz):
        return float_int(A(*wyraz)) or float_int(B(*wyraz)) or float_int(C(*wyraz)) or float_int(D(*wyraz))

    return rek1(T,len(T))

print(zad23([1,2,3,4,5,6]))
