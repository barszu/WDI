class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

# def dodaj_1(ob): #->1(dodaj jeden na przod) 0(nic nie rob)
#     if ob is None : return 1
#     if ob.val == None: ob = ob.next
    
#     ob.val = ob.val+dodaj_1(ob.next)
#     if ob.val >= 10:
#         ob.val = 0
#         return 1
#     else: return 0

def dodaj_1(ob,h): #->1(dodaj jeden na przod) 0(nic nie rob)
    if ob is None : return 1
    if ob.val == None: ob = ob.next
    
    ob.val = ob.val+dodaj_1(ob.next,h)
    if ob.val >= 10:
        ob.val = 0
        if h.next == ob:
            new = Node(1)
            new.next = ob
            h.next = new
            return
        else: return 1
        
        
    else: return 0




# b=Node(9)
a=Node(9)
h=Node(None,a)
dodaj_1(h,h)
print_all(h)






def zad9(el1):
    if el1 == None :
        d = Node(1,None)
        return d
    
    if el1.val != 9 :
        el1.val = el1.val + 1
        return el1
    else:
        el1.val = 0
        # zad9(el1.next)
        el1.next = zad9(el1.next)
    
    return el1

# ITERACYJNE ROZWIAZANIE
def zad9(el):
    if el == None :
        d = Node(1,None)
        return d
    
    a = el
    while a != None :
        if a.val != 9 :
            a.val = a.val + 1
            break
        else:
            a.val = 0
            if a.next == None:
                e = Node(1,Node)
                a.next = e
    return el
            
            