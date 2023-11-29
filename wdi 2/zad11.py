num = input(">>> ")
is_ascending = True
for id in range(1 , len(num)) :
    if int(num[id-1]) > int(num[id]):
        is_ascending = False
if is_ascending :
    print("cyfry w liczbie sa rosnace")
else:
    print("cyfry w liczbie NIE są rosnace")
