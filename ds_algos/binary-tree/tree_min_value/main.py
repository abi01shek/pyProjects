# tree min value
# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.
import math

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Using a stack recursively for practice
def tree_min_value(root):
    # exit condition: leaf node
    if(root.left is None and root.right is None):
        return root.val
    # sub tree conditions
    left_tree_min = math.inf
    right_tree_min = math.inf
    if(root.left is not None):
        # find minimum value in left side depth first
        left_tree_min = tree_min_value(root.left)
    if(root.right is not None):
        # find minimum value in right side depth first
        right_tree_min = tree_min_value(root.right)
    # Compare current value with minimum values on either sides
    min_val = root.val
    min_val = min_val if (min_val < left_tree_min) else left_tree_min
    min_val = min_val if (min_val < right_tree_min) else right_tree_min
    return min_val

# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1
# print(tree_min_value(a)) # -> -2

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

print(tree_min_value(a)) # -> 3
