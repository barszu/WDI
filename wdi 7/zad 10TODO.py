class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

#zakladam ze sa tych samych wymiarow
def dodaj_ll(h1,h2):
    h = Node(None)
    def rek(p,q,higher_obj=None): #->zwracane sa reszty i dodawane
        nonlocal h1,h2,h
        if p is None: return 0
        new = Node(-1,higher_obj)
        new.val = p.val+q.val+rek(p.next,q.next,new)
        if new.val <= 9: return 0
        else:
            if h1.next != p:
                a = new.val 
                new.val = new.val%10
                return a//10
            else:
                #wstawic obiekt miedzy h a 1st obiekt
        

#backup
def dodaj_ll(h1,h2):
    h = Node(None)
    def rek(p,q):
        nonlocal h1,h2,h
        if p.next is not None: r = rek(p.next,q.next)
        else: r = 0
        
        new = Node(p.val+q.val+r)
        if new.val <= 9: return 0

        else:
            a = new.val 
            new.val = new.val%10



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