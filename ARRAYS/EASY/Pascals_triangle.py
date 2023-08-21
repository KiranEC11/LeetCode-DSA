"""
118. Pascal's Triangle

Link: https://leetcode.com/problems/pascals-triangle/
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            start = [1]
            if not triangle:

                triangle.append(start)
            else:
                prev_row = triangle[-1]
                m = len(prev_row)
                j=0
                while j<m-1:
                    start.append(prev_row[j] + prev_row[j+1])
                    j +=1
                start.append(1)
                triangle.append(start)
        return triangle
                

