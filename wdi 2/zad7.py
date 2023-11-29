inputted_num = int(input(">>> "))

n = 1
while True:
    a = n*n + n + 1
    k = 1  
    if inputted_num%a == 0 :
        print("jakas wielokrotnosc wyrazu ciagu = {0}".format(inputted_num))
        break
    if inputted_num < a :
        break
    n += 1