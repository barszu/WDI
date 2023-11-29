def contains(T,w,k):
    # if k>=0 and k<8 and w>=0 and w<8 : return True
    l =len(T)
    if 0 <= k < l and 0 <= w < l : return True
    else: return False


#uzyty back tarcking


def kings_walk(T , w=0 , k=0 , n=1):
    T[w] [k] = n
    
    if n == len(T)**2: return True
    
    jumps = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,1)]
    for (dw , dk) in jumps:
        next_w = dw + w
        next_k = dk + k
        if contains(T, next_w , next_k ) and T[next_w] [next_k] == 0 :
            if kings_walk(T , next_w , next_k , n+1): 
                return True
    
    T[w] [k] = 0
    return False

T2 = [[0 for _ in range(8) ] for _ in range(8)]
kings_walk(T2)
for row in T2: print(row)