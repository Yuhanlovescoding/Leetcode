''' Solution 1'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]




 '''Solution 2'''
class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            complete = target - nums[i]
            if complete in nums and nums.index(complete) != i:
                return [i,nums.index(complete)]
    
sol = Solution()
print(sol.twoSum([3,2,4], 6))