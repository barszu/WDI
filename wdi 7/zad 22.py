class Node :
    def __init__ (self, val:int , next=None):     #obiekt wskazuje na none(obiekt)
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

def has_cycle(head):
    if head is None: return False
    pointer = head.next if head.val == None else head
    fast = pointer
    slow = pointer
    while True :
        try: 
            slow = slow.next
            fast = fast.next.next
        except: return False
        
        if fast == slow: return True


c=Node(15)
b = Node(10,c)
a = Node(5,b)
h = Node(None)
print(has_cycle(h))
