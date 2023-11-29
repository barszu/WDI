
max_c = 0
fstart_num = 0

for start_n in range(3 , 10**5):
    a = float(start_n)
    b = (a%2)*((3*a) + 1)+(1-(a%2))*(a/2)
    condition = True
    c = 0
    while condition  :
        c += 1
        if b == 1.0 :
            if c >= max_c:
                max_c = c
                fstart_num = start_n
            condition = False   
        a , b = b , (a%2)*((3*a) + 1)+(1-(a%2))*(a/2)
        

print(fstart_num)
        