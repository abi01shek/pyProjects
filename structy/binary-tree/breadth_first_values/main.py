from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


def breadth_first_values(root):
    queue = deque([root])
    values = []
    while(queue):
        curr = queue.popleft()
        values.append(curr.val)
        if(curr.left):
            queue.append(curr.left)
        if(curr.right):
            queue.append(curr.right)
    return values


breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
