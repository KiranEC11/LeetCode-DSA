"""
Unique Paths

https://leetcode.com/problems/unique-paths/description/

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # rights_to_take = n-1
        # downs_to_take = m-1
        # total_steps_to_take = m+n-2
        def factorial(x):
            mult = 1
            for i in range(1,x+1):
                mult *= i
            return mult
        
        return int(factorial(m+n-2)/(factorial(n-1)* factorial(m-1)))