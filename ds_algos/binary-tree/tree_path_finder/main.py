"""
tree path finder
Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Note the splat * operator in list is expensive O(n)
# and so program itself is O(n^2)
def path_finder(root, target):
    if(root is None):
        return None

    if(root.val == target):
        return [root.val]

    left_path = path_finder(root.left, target)
    if left_path is not None:
        # found a path to the left
        return [root.val, *left_path]

    right_path = path_finder(root.right, target)
    if right_path is not None:
        # found a path to the right
        return [root.val, *right_path]

    # no paths found under the current node
    return None

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

path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]

