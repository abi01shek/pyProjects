# tree includes
# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.
from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# using queue as it reduces number of lookups
# if key is earlier in the tree
def tree_includes(root, val):
    if(root is None):
        return False

    queue = deque([root])
    while(queue):
        curr = queue.popleft()
        if(curr.val == val):
            return True
        if(curr.left is not None):
            queue.append(curr.left)
        if(curr.right is not None):
            queue.append(curr.right)
    return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

print(tree_includes(a, "e")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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
print(tree_includes(a, "a")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

print(tree_includes(a, "n")) # -> False

print(tree_includes(None, "b")) # -> False
