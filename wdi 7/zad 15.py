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

def zapis_3(num): #->str
    w = ""
    while num != 0:
        w += str(num%3)
        num = num//3
    return w

def special_cond(num):
    w = zapis_3(num)
    return w.count("1") > w.count("2")


def fn(h):
    a=h
    while a.next is not None:
        if special_cond(a.next.val):
            #usun ja
            a.next = a.next.next
        a = a.next

d = Node(4,None)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)
h = Node(None,a)
fn(h)
print_all(h)