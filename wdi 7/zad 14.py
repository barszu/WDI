class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def print_all(p):
    if p is not None:
        print(p.val)
        print_all(p.next)

def fn(h):
    a = h
    while True:
        if a.next.next.val % a.next.val == 0:
            #usun element a.next
            a.next = a.next.next
        
        a = a.next
        if a.next is None: break
        elif a.next.next is None: break


d = Node(4,None)
c = Node(2,d)
b = Node(3,c)
a = Node(1,b)
h = Node(None,a)
fn(h)
print_all(h)