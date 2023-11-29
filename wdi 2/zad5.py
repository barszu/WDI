def mask_gen(lenth):
    
    def bins(num , lenth ):
        #returns binary representation with 0 in front of to fullfill
        bins = ""
        while num != 0:
            bins += str( num%2 )
            num = num//2
            
        bins = bins[::-1]
        while len(bins) < lenth :
            bins = "0" + bins
        return bins
    
    mask_list = [bins(i , lenth) for i in range(2**(lenth))]
    return mask_list


def zad5( num , d):
    num = str(num)
    l = len(num)
    maski = mask_gen(l)
    c = 0
    # 0 - nie ma cyfry
    # 1 - jest cyfra
    for x in maski:
        if x.count("0") < l and x.count("1") < l :
            el = ""
            for id in range(l):
                if x[id] == "1" :
                    el += num[id]
            if int(el)%d == 0 : c += 1
    return c
            
print(zad5(2315 , 7))
