# depth first values
# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.


def depth_first_values_recr(root):
    if(root is None):
        return []
    left_values = depth_first_values_recr(a.left)
    right_values = depth_first_values_recr(a.right)
    return [root.val, *left_values, *right_values]

def depth_first_values(root):
    stack = [root]
    values = []

    while(stack):
        cnode = stack.pop()
        values.append(cnode)
        if cnode.left:
            stack.push(cnode.left)
        if cnode.right:
            stack.push(cnode.right)
    return values

