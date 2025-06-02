def longest_streak(head):
    pval = head.val
    head = head.next
    longest_streak = 0
    current_streak = 1
    while(head is not None):
        cval = head.val
        if(cval == pval):
            # continuing current streak
            current_streak = current_streak + 1
        else:
            # starting a new streak
            current_streak = 1
            pval = cval
        head = head.next
        if(current_streak > longest_streak):
            longest_streak = current_streak

    return longest_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a)) # 3


a = Node(5)
b = Node(5)

a.next = b

# 5 -> 5

print(longest_streak(a)) # 2
