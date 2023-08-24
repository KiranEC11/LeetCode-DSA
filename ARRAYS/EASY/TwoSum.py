"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/

"""
"""
1. BRUTE FORCE METHOD
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
        
        
""""
COMPLEMENT METHOD
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # num = nums[i]
            # idx = i
            complement = target - nums[i]
            if complement in nums and nums.index(complement)!=i:
                
                return [i,nums.index(complement)]
            
"""

"""