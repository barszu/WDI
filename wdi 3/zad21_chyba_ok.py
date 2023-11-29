def mask_gen_3(lenth):
    
    def bins(num , lenth ):
        #returns binary representation with 0 in front of to fullfill
        bins = ""
        while num != 0:
            bins += str( num%3 )
            num = num//3
            
        bins = bins[::-1]
        while len(bins) < lenth :
            bins = "0" + bins
        return bins
    
    mask_list = [bins(i , lenth) for i in range(3*(lenth))]
    return mask_list

def nwd(a,b):
    while True:
        a , b = b , a%b
        if b == 0 : return a


def trojki(tab):
    N = len(tab)
    maski = mask_gen_3(N)
    #sprawdzacz masek
    kody = [ "111" , "1011" , "1101" , "10101" ]
    c = 0
    for mask in maski:
        if mask.count("1") == 3 :
            #dokladnie tutaj jest jedna maska
            for kod in kody:
                if kod in mask :
                    #wlasciwa czesc
                    odp = [None]*3
                    #dekoder
                    i = 0
                    for id in range(N) :
                        if mask[id] == "1" :
                            odp[i] = tab[id]
                            i += 1
                    if nwd(odp[0],nwd(odp[1],odp[2])) == 1:
                        c += 1
    return c