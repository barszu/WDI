class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

#rekurencyjne odwrocenie listy dziala jak cia rekurencyjny 
# mam el a dalej nie wiem co jest
# i to na bierzaca generuje
def reverse(p):
    if p.next is None: return p
    else:
        prev = reverse(p.next)
        q = prev
        while q.next != None: 
            q = q.next
        
        q.next = p
        p.next = None
        return prev

# TODO zrob odwracanie ale lista do odwracania ma guardiana


z = Node(15)
y = Node(10 , z)
x = Node(5,y)
g = Node(None,x) #guardian

def print_obj(g):
    a = g#.next
    while a is not None:
        print(a.val)
        a = a.next
    return

print_obj(g)
print("-reverse-")
reverse(g)
print_obj(g)
print("koniec")
#print(g.next.val , x.next.val , y.next.val , z.next.val )