"""
229. Majority Element II
    Given an integer array of size n, 
    find all elements that appear more than ⌊ n/3 ⌋ times.
https://leetcode.com/problems/majority-element-ii/description/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # calculate floor n/3
        n = len(nums)
        m = n//3
        output_list = []
        dic = {}

        for i in range(n):
            if dic:
                if nums[i] not in dic.keys():
                    dic[nums[i]] = 1
                    if dic[nums[i]]>m:
                        output_list.append(nums[i])
                else:
                    dic[nums[i]] +=1
                    if dic[nums[i]]>m:
                        output_list.append(nums[i]) if nums[i] not in output_list else None
            else:
                # initialisation
                dic[nums[i]] = 1
                if dic[nums[i]]>m:
                    output_list.append(nums[i])
        
        return output_list
