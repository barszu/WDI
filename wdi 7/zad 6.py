class Node:
    def __init__(self,v,next=None): #None as obj not a value
        self.val = v
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

def attach(h,val):
    a = h
    while a.next is not None:
        a = a.next
    #a pokazuje na ostatni el
    new = Node(val)
    a.next = new