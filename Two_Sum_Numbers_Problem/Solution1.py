'''Approach 1: o(n^2) Time Complexity and O(1) Space Complexity'''
def twoNumberSum(array, targetSum):
    # Write your code here
    for i in range(0,len(array)-1):
		  for j in range(i+1,len(array)):
			  addition = array[i]+array[j]
			  if addition == targetSum:
				  if array[i]<array[j]:
					  return [array[i],array[j]]
				  else:
					  return [array[j],array[i]]
	  return []


''' Approach 2 : O(n) Time Complexity and O(n) Space Complexity'''
def twoNumberSum(array, targetSum):
    # Write your code here
    num = {}
	
	  for val in array:
		  if targetSum-val in num:
			  if targetSum-val < val: 
				  return [targetSum-val,val]
			  else:
				  return [val,targetSum-val]
		  else:
			  num[val] = True
	  return []

'''Approach 3: O(nlogn) Time Complexity and O(1) Space Complexity'''

def twoNumberSum(array, targetSum):
    # Write your code here
	
	left = 0
	right = len(array)-1
	
	array.sort()
	
	while(left<right):
		addition = array[left]+array[right]
		if addition == targetSum:
			return [array[left],array[right]]
		elif addition < targetSum:
			left+=1
		else:
			right-=1
	return []

