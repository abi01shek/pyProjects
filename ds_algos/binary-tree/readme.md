If you want to do depth first search use stack
	stack.append() is pushing into stack
	stack.pop() is popping top value from the stack
Note: instead of stack you can also use recursion
Recursion does depth first search in binary tree.
I find recursion easier than stack because using stack
we need to identify the variables that have to be pushed
With recursion, all variables are pushed into the stack

If you want to do breadth first search use queue
	queue.append() is adding to input of queue
	queue.popleft is removing from output of queue

For both traversal, start by adding the root. Pop the root out
and add the left followed by the right into the appropriate data
structure. The data structure will take care of right order of
traversal

