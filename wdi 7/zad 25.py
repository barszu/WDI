class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def ile_el_przed_cyklem(pointer:Node):
    fast = pointer
    slow = pointer
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow: break
    counter=0
    fast = pointer
    while fast is not slow:
        fast = fast.next
        slow = slow.next
        counter += 1
    return counter

def ostatni_przed_cyklem(pointer:Node): #->Node|None #doiterowanie do tego el
    I = ile_el_przed_cyklem(pointer)
    I -=1
    if I<0: return None
    temp = pointer
    while I>0:
        I = I-1
        temp = temp.next
    return temp
    

c=Node(15)
b = Node(10,c)
a = Node(5,b)
h = Node(None,a)
c.next = a
print(ostatni_przed_cyklem(h))