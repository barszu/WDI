# c = 0
# for num in range(10**5 , 10**6):
#     flag = True
#     for i in str(num):
#         if i not in ["0",'1','2','3']: 
#             flag = False
#             break
#     if num%6==0 and flag: c+=1
# print(c)

# print(3*4*4*4*2)

def zad():
    c = 0
    def rek(num='' ,l=0 ):
        nonlocal c
        if l == 5 :
            if int(num) % 6 == 0 : 
                c += 1
            return False
        
        return rek(num+"0",l+1) or rek(num+"1",l+1) or rek(num+"2",l+1) or rek(num+"3",l+1)
    rek()
    return c

print(zad()/(3*4*4*4*2))