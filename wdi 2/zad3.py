num = input(">>> ")

if num[:len(num)//2] == (num[((len(num) +1) // 2) :])[::-1] :
    print("{0} is a palidrome ".format(num))
else:
    print("{0} is NOT a palidrome".format(num))
    
bin_num = bin(int(num))[2:]

if bin_num[:len(num)//2] == (bin_num[((len(num) +1) // 2) :])[::-1] :
    print("{0} is a palidrome in binary format".format(num))
else:
    print("{0} is NOT a palidrome in binary format".format(num))