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


def is_prime(num):
    if num%2 == 0 or num%3 == 0 : 
        return False
    from math import isqrt
    #dla duzych liczb
    if num > 100:
        k = 1
        while (6*k - 1 < isqrt(num) + 1):
            if num%(6*k - 1) == 0 or num%(6*k + 1) == 0 :
                return False
            k += 1
        else: return True
    #dla mniejszych liczb
    else:
        for d in range(2 , isqrt(num) + 1):
            if num%d == 0 : return False
        else: return True

def zad14(a , b):
    a , b = str(a) , str(b)
    c = 0
    l_a = len(a)
    l_b = len(b)
    l = l_a + l_b
    # 0 - cyfra z liczby a
    # 1 - cyfra z liczby b
    maski = mask_gen(l)
    
    for mask in maski:
        if mask.count("0") == l_a and mask.count("1") == l_b :
            num = ""
            id_a = 0
            id_b = 0
            for i in range(l):
                if mask[i] == "0" :
                    num += a[id_a]
                    id_a += 1
                elif mask[i] == "1" :
                    num += b[id_b]
                    id_b += 1
            if is_prime(int(num)) : c += 1
    return c
            
print(zad14(123 , 76))