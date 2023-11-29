class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def cycle_length(pointer):
    counter = 0
    fast = pointer
    slow = pointer
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast is slow: break
    fast = fast.next.next
    slow = slow.next
    counter += 1
    while fast is not slow:
        counter += 1
        fast = fast.next.next
        slow = slow.next
    return counter


c=Node(15)
b = Node(10,c)
a = Node(5,b)
h = Node(None,a)
c.next = a
print(cycle_length(h))
