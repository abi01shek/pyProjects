class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
    return univ_recr(head.next, head.val)

def univ_recr(head, prev_val):
    if(head is None):
        return True
    if(prev_val != head.val):
        return False
    return True & univ_recr(head.next, head.val)



a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

assert is_univalue_list(a) == True


a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

assert is_univalue_list(a)== False
