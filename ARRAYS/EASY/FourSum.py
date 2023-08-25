"""
here we need to return all the unique lists of quadraples which add upto target.
In twoSum problem we returned index of pairs. That too we assumed there is only
one solution.

So things are different here.
we define a different twosum function also here, which will be suitable for 
our purpose 
_______________________
4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


"""

class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        pairs = set()
        for num in nums:
            complement = target - num
            if complement in seen:
                pairs.add(tuple(sorted([num, complement])))
            seen.add(num)
        return [list(pair) for pair in pairs]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        list_output = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total = nums[i]+nums[j]
                nums1 = nums[:i]+nums[i+1:j]+nums[j+1:]

                two_sum_list = self.twoSum(nums1, target- total)
                if two_sum_list:
                    for sublist in two_sum_list:
                        nums2 = sublist+[ nums[i], nums[j] ]
                        nums2.sort()
                        if nums2 not in list_output:
                            list_output.append(nums2)
        
        return list_output


"""
the above approach requires more time. It can be minimised with a better code
"""


"""
another better approach
"""             
        
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()   ###### very important point--> sort list if we dont want list with same items
        i = 0
        L = len(nums)
        res = []
        while i < L-3:
            j = i+1
            while j < L-2:
                left = j+1    ## method of sliding window [left, right]
                right = L-1
                new_target = target-nums[i]-nums[j]
                while left<right:
                    if nums[left]+nums[right] > new_target:
                        right-=1
                    elif nums[left]+nums[right] < new_target:
                        left+=1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        temp_left = nums[left]
                        temp_right = nums[right]
                        while(left<right and nums[left]==temp_left):
                            left+=1
                        while(left<right and nums[right]==temp_right):
                            right-=1
                while j < L-3 and nums[j] == nums[j+1]:
                    j+=1
                j+=1
            while i < L-4 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res