"""
all tree paths
Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def all_tree_paths(root):
    if(root is None):
        return []
    if (root.left is None) and (root.right is None):
        return [root.val]
    path_list = []
    left_path_list = all_tree_paths(root.left)
    right_path_list = all_tree_paths(root.right)
    for sub_path in left_path_list:
        path_list.append([root.val, *sub_path])
    for sub_path in right_path_list:
        path_list.append([root.val, *sub_path])
    return path_list


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

print(all_tree_paths(a))

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#         a
#      /    \
#     b      c
#   /  \      \
#  d    e      f
#      / \    /
#     g  h   i

print(all_tree_paths(a)) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e', 'g' ],
#   [ 'a', 'b', 'e', 'h' ],
#   [ 'a', 'c', 'f', 'i' ]
# ]
