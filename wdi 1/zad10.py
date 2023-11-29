def d_list(number):
    from math import isqrt
    d_list = set([ 1 , number ])
    for d in range(2 , isqrt(number)+1):
        if number % d == 0 :
            d_list.add( d )
            d_list.add(int(number/d))
    return sorted(list(d_list))

def sumOFnum(list_):
    c = 0
    for i in list_[0:-1] :
        c += int(i)
    return c
    

end_num = 10**6
searched_num = []
for temp_num in range (2 , end_num):
    print("searching ... {0:%}".format(temp_num/end_num))
    if sumOFnum(d_list(temp_num)) == temp_num :
        searched_num.append(temp_num)
print(searched_num)