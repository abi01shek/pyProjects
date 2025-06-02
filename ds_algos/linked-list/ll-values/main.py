# linked list values
# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
    ret_list = []
    curr = head
    while(curr != None):
        ret_list.append(curr.val)
        curr = curr.next
    return(ret_list)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

assert linked_list_values(a) == [ 'a', 'b', 'c', 'd' ]

x = Node("x")
y = Node("y")

x.next = y

# x -> y

assert linked_list_values(x) == [ 'x', 'y' ]

q = Node("q")

# q

assert linked_list_values(q) == [ 'q' ]


assert linked_list_values(None) == [ ]
