el_list = [1 , 1]
id = 1 
while el_list[-1] < 10**6 :
    a = el_list[id - 1]
    b = el_list[id]
    a , b = b , a+b
    el_list.append(b)
    id += 1
if el_list[-1] > 10**6:
    el_list.pop(-1)
print(el_list)