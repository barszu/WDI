class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_all(p):
    if p is not None:
        print(p.val , end="->")
        print_all(p.next)
    else: print("\n")

##(set)ll:str
#dodaj el:str i zwroc boola czy faktycznie zostal dodany
def fn(h,key):
    a = h.next
    while a.next is not None:
        if a.val == key: #zawiera
            #to nic nie robie
            return False
        if key > a.val : return False
        a = a.next
    #a wiec nie ma to tzreba dodac
    #jestesmy na ostatnim el
    new = Node(key)
    a.next = new
    return True

