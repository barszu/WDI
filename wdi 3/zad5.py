ciag = []
while True:
    a = int(input(">"))
    if a == 0 : break
    ciag.append(a)

ciag.sort(reverse = True)
i = 0
for id in range(1 , len(ciag)) :
    if ciag[id] != ciag[id-1]:
        i += 1
        if i == 3:
            print(ciag[id-1])
            break
