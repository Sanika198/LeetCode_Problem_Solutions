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
