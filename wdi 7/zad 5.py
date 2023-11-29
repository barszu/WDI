class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def print_all(a:Node):
    while a is not None:
        print(a , end=" ") #w jednej linijce wypisuje
        a = a.next

def print_tab(T):
    for i in T : print(i , end=" ")

#ogarnij kod
def split(ll:Node):
    #czy jest guardian czy go nie ma
    curr = ll.next if ll.val == None else ll #pomijam tego guardiana
    #tablica co ma link listy
    part = [ Node(None) for _ in range(10) ] #ma el co maja ostatnia cyfre ta sama
    #napchane guardianami
    lasts = [n for n in part] #ostatni el w danej liscie
    while curr is not None: #iteracja po link liscie
        nex = curr.next
        i = curr.val % 10
        lasts[i].next = curr #nadpisuje lasts
        lasts[i] = lasts[i].next
        lasts[i].next = None #odciecie linku
        
        curr = nex
    
    for l in part:
        print_all(l)
        print("")
    
    print("---")
    #teraz laczymy te 10 link list
    res = Node(None) #guardian klejonego
    for i in range(10-1):
        # do ostatniego el link listy doczepiam poczatek nowej
        lasts[i].next = part[i+1].next #next skipuje guardiana
    
    print_all(part[0])
    # print("\nparts:")
    # print_tab(part)
    # print("\nlasts:")
    # print_tab(lasts)
    return 


c = Node(15)
b = Node(10 , c)
a = Node(5 , b)


split(a)