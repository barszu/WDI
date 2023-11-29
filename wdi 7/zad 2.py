class Node:
    def __init__(self,v,next=None): #None as obj not a value
        self.val = v
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

def find_obj_by_inx(h,i): #->Node
    #on istnieje pod tym id juz
    a = h
    ii = 0
    while ii < i:
        a = a.next
        ii += 1
    return a

def fill(h,i): #zwraca ostatni na ktory patrzylo
    l = 0
    a = h
    while l<i: #dopisz wyrazy typu None
        new = Node(None)
        a.next = new
        l += 1
        a = a.next
    return a

def init(T): #T:tab:(id,int):
    from math import inf
    h = Node(inf)
    l = 0
    last = h
    for (idx,val) in T:
        if idx > l : 
            last = fill(last,idx)
            l = idx
        find_obj_by_inx(h,idx).val = val
    return h

start = init([(20,18),(5,0),(8,14)])
print_all(start)

def find_val_at_id(h,i):
    return find_obj_by_inx(h,i).val


def podstaw_at_id(h,i,val):
    find_obj_by_inx(h,i).val = val

podstaw_at_id(start,6,1000)
print(find_val_at_id(start,6))