def count_samogloski(str_):
    samogloski = ["a","e","o","i","y","u"]
    c = 0
    for znak in str_:
        if znak in samogloski: c += 1
    return c

def ascii_sum(T):
    suma = 0
    for el in T:
        suma += ord(el)
    return suma

def wydobadz(str_ , sam=True ):  #sam bool TRUE-FALSE (samogloska , SPOLgloska)
    samogloski = ["a","e","o","i","y","u"]
    wybrane = ""
    if sam:
        for symbol in str_ :
            if symbol in samogloski :
                wybrane += symbol
    else:
        for symbol in str_ :
            if not symbol in samogloski :
                wybrane += symbol
    return wybrane

def rek_doczepiacz_spol(spol_T , r , i=0): #-> TRUE/FAlSE (czy moge wogole jakos to podoczepiac czy nie)
    if r < 0 or len(spol_T) == i : return False
    if r == 0 : return True
    
    # return doczep/niedoczep
    return rek_doczepiacz_spol(spol_T , r-ord(spol_T[i]) , i+1) or rek_doczepiacz_spol(spol_T , r , i+1)

def wyraz(s1:str,s2:str): #-> bool# z s2 buduje s3 i s3 == s1
    s1_sam = count_samogloski(s1)
    s1_ascii_sum = ascii_sum(s1)
    s2_sam = count_samogloski(s2)
    if s2_sam < s1_sam : return False
    elif s2_sam == s1_sam :
        s1_ascii_sum -= ascii_sum(wydobadz(s2)) #s3 = tablica SAMOglosek z s2 wszytskich --> ale tak naprawde zachowam tylko kod ascii tego
        # rekurencyjnie doczepiaj SPOLgloski
        return rek_doczepiacz_spol(wydobadz(s2 , False) , s1_ascii_sum )
    
    #normalny przypadek -> rek kombinacja samoglosek --> rekurencyjnie doczepiam spolgloski
    def rek_wybieracz_sam(sam_T , k , suma_docelowa , i=0 ): #k - ile pozostalo do wyboru samoglosek
        nonlocal s2
        if k == 0 : 
            # return /str/ -> podoczepiam spolgloski i sprawdze -> main return bool
            return rek_doczepiacz_spol(wydobadz(s2 , False) , suma_docelowa )
        elif k < 0 or len(sam_T) == i : return False
        # body
        # return biore/niebiore
        return rek_wybieracz_sam(sam_T , k-1 , suma_docelowa-ord(sam_T[i]) , i+1  ) or rek_wybieracz_sam(sam_T , k  ,suma_docelowa , i+1)
    
    return rek_wybieracz_sam(wydobadz(s2) , s1_sam , s1_ascii_sum)

print(wyraz("exeeeeeeeeeeeeeeeeeeeeeeeee" , "exealbodpi"))
