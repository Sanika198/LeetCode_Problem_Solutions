'''Approach 1: o(n^2) Time Complexity and O(n) Space Complexity'''

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []
        start = 0
        nums.sort()
        for start in range(len(nums)):
            if (nums[start]>0 or nums[start-1]==nums[start]) and start!=0:
                continue
            left = start+1
            right = len(nums)-1
           
            while(left<right):
                temp=[]
                add = nums[start] + nums[left]+ nums[right]
                
                if add == 0:
                    temp = [nums[start],nums[left],nums[right]]
                    #if temp not in result:
                    result.append(temp)
                    left +=1
                    right -=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif add<0:
                    left += 1
                elif add>0:
                    right -=1
                
            start += 1           
        return result
        
 '''Approach 2: o(n^2) Time Complexity and O(n) Space Complexity'''
 
 class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, temp = [], []
        start = 0
        nums.sort()
        for start in range(len(nums)):
            if (nums[start]>0 or nums[start-1]==nums[start]) and start!=0:
                continue
            
            self.twoSum(nums,start,nums[start],result)

        return result

    def twoSum(self,nums,new,target,res):
        dic={}
        add, i = 0, new+1
        
        while i<len(nums):
            add = -target - nums[i]
            if add in dic:
                res.append([add,nums[i],target])
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
            dic[nums[i]]=i
            i+=1
 
