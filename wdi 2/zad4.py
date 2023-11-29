def num_is_only_div(num , list_of_div):
    for d in list_of_div :
        while num % d == 0 :
            num //= d
    return (num == 1)

def zad4(n):
    c = 0
    for num in range(1 , n + 1):
        if num_is_only_div(num , [2,3,5]):
            c += 1
    return c

print(zad4(25))
