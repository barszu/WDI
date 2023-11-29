class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

def fn(h,key):
    a = h
    while a.next.next is not None:
        if a.next.val == key: #zawiera
            #to usuwam
            a.next = a.next.next
            return
        a = a.next
    #a wiec nie ma to tzreba dodac
    a = a.next #jestesmy na ostatnim el
    new = Node(key)
    a.next = new
    return

d = Node(4,None)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)
h = Node(None,a)
fn(h,7)
fn(h,1)
print("---")
print_all(h)