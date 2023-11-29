#wieza hanoi
def hanoi(A ,B , C , n):
    if n == 0 : return
    hanoi(A,C,B,n-1)
    el = A[-1]
    A.pop() #wyrzucam najwyzszy z A
    B.append(el) # dodaje na wieze B
    hanoi(C,B,A,n-1)