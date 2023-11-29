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


c=Node(15)
b = Node(10,c)
a = Node(5,b)
h = Node(None,a)
c.next = a
print(ile_el_przed_cyklem(h))