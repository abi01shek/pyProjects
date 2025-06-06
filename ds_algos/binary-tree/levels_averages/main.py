"""
level averages
Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.
"""
from collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# breadth first search: use queue
def level_averages(root):
    level_dict = {}
    queue = deque([(root,0)]) # root is in level 0
    while(queue):
        (curr,curr_level) = queue.popleft()
        if((curr_level,"sum") not in level_dict):
            level_dict[(curr_level,"sum")] = curr.val
            level_dict[(curr_level,"count")] = 1
        else:
            level_dict[(curr_level,"sum")] += curr.val
            level_dict[(curr_level,"count")] += 1

        next_level = curr_level+1
        if(curr.left is not None):
            queue.append((curr.left,next_level))
        if(curr.right is not None):
            queue.append((curr.right, next_level))

    level_num = 0;
    level_avgs = []
    while True:
        if (level_num, "sum") in level_dict:
            level_avgs.append(level_dict[(level_num, "sum")]/level_dict[(level_num, "count")])
            level_num = level_num + 1
        else:
            break

    return level_avgs

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

level_averages(a) # -> [ 3, 7.5, 1 ] 
