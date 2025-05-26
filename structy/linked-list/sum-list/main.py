class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
    sum = 0;
    while(head):
        sum = sum + head.val
        head = head.next
    return(sum)



a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
