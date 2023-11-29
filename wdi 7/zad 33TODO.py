class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)
    
    def generate(self,T): #self jako start doklejania
        a = self
        for new_val in T:
            new_obj = Node(new_val)
            a.next = new_obj
            a = a.next
        return self
    
    def print_all(self,p=None):
        if p is not None : a=p
        else: a=self
        while True:
            print(a.val , end="->")
            a = a.next
            if a is None: 
                print("\n")
                return

# relacja < (dla ostatnich liter) uzyuwaj reversed str
def wstaw(a,val): #-> bool #czy sie udalo wstawic , wskaznik na nowy el
    start = a #wstawiaj po a
    # cnt = 0
    while a.next is not start:
        if ord(a.val[-1]) < ord(val[0]) and ord(val[-1]) < ord(a.next.val[-1]):
            new = Node(val)
            a.next , new.next = new , a.next
            a = new
            return True
        # cnt += 1
        a = a.next
    
    if ord(a.val[-1]) < ord(val[0]) and ord(val[-1]) < ord(a.next.val[-1]):
        new = Node(val)
        a.next , new.next = new , a.next
        a = new
        return True
    return False

# Node("bartek").generate(["leszek","marek","ola","zosia"])
a=Node("bartek")
b=Node("leszek")
c=Node("larek")
a.next = b
b.next = c
c.next = a
print(wstaw(a,"ola"))
print(a)
#TODO jak przestawić wskaznik pokazujący na nowy 