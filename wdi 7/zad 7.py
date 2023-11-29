class Node:
    def __init__(self,v,next=None): #None as obj not a value
        self.val = v
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

def del_last(h,val):
    a = h
    while a.next.next is not None:
        a = a.next
    #a jest przed ostatnim el
    a.next = None