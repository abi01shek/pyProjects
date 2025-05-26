# add lists
# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def add_lists(head_1, head_2):
    cval1 = 0
    cval2 = 0
    carry = 0
    dummy_head = Node(None)
    tail = dummy_head
    while(True):
        if((head_1 is None) and (head_2 is None)):
            break

        if(head_1 is None):
            cval1 = 0
        else:
            cval1 = head_1.val

        if(head_2 is None):
            cval2 = 0
        else:
            cval2 = head_2.val

        sumval = cval1 + cval2 + carry
        if(sumval > 10):
            sumval = sumval - 10
            carry = 1
        else:
            carry = 0

        tail.next = Node(sumval)
        tail = tail.next

        if head_1 is not None:
            head_1 = head_1.next
        if head_2 is not None:
            head_2 = head_2.next

    return(dummy_head.next)


#   39
# + 47
# ----
#   86

a1 = Node(9)
a2 = Node(3)
a1.next = a2
# 9 -> 3

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

r = add_lists(a1, b1)
while(r is not None):
    print(r.val, "-> ", end = '')
    r = r.next
