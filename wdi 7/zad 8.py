class Node:
    def __init__(self,v,next=None): #None as obj not a value
        self.val = v
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

#ll nie pusta
def fn(h):
    a = h.next if h.val == None else h
    k_next = 2
    while a.next is not None:
        if k_next%2==0:
            a.next = a.next.next
            k_next += 2
        else: k_next += 1
        a = a.next
        if a is None: break
    return h

# d = Node(4)
# c = Node(3)
# b = Node(2)
a = Node(1)
h = Node(None,a)

fn(h)
print_all(h)