"""
169. Majority Element

https://leetcode.com/problems/majority-element/description/
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        
        for i in range(len(nums)):
            if count_dict:
                if nums[i] not in count_dict.keys():
                    count_dict[nums[i]] = 1
                else:
                    count_dict[nums[i]] += 1
                    if count_dict[maj_elem]<count_dict[nums[i]]:
                        maj_elem = nums[i]
            else:
                maj_elem = nums[i]   # initialisation
                count_dict[nums[i]] = 1
            
            
        return maj_elem