def numsys(a , base_of_sys):
    #returns coded num in diferent system as string
    code = ""
    while a > 0 :
        code += str(a%base_of_sys)
        a = a//base_of_sys
    return code[::-1]

def zad20(a , b):
    for s in range(2 , 16 + 1):
        a_s = numsys(a , s)
        b_s = numsys(b , s)
        rozlaczne = True
        #sprawdzanie czy cyfry sie zawieraja
        for i in a_s:
            if i in b_s : 
                rozlaczne = False
                break
        if rozlaczne == True:
            return s , a_s , b_s
    return "brak takiego sys"

print(zad20(123 , 126))