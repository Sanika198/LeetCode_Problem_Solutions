'''Approach 1: Iterative Approach 
Time Complexity: O(log(n)) Space Complexity:O(1)'''

def ClosestNodeValueInBst(tree, target):
    # Write your code here.	
	root = tree
	close = root.value
	while(root!=None):
		if root.value == target: 
			return root.value
		if abs(target-root.value) < abs(target - close) :
			close = root.value
		if root.value<target:
			root = root.right
		else:
			root = root.left
	return close
		
'''Approach 2: Recursive Approach
Time Complexity: O(log(n)) Space Complexity:O(log(n))'''

def ClosestNodeValueInBst(tree, target):
    # Write your code here.	
	return closenode(tree,target,float("inf"))
def closenode(tree,target,close):
	if tree==None:
		return close
	if abs(target-tree.value) < abs(target - close) :
		close = tree.value
	if tree.value<target:
		return closenode(tree.right,target,close)
	elif tree.value>target:
		return closenode(tree.left,target,close)
	else:
		return close
	
		

