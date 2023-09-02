"""
151. Reverse Words in a String
Medium
7.2K
4.9K
Companies
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""

class Solution:

    #method 1
    # def reverseWords(self, s: str) -> str:
    #     s = s.strip()
    #     s=s.split()
    #     ll = []
    #     for i in range(len(s)-1,-1,-1):
    #         ll.append(s[i])
    #     return " ".join(ll)

    #method2
    # def reverseWords(self, s: str) -> str:
    #     s = s.strip()
    #     s=s.split()
    #     s= s[::-1]
    #     return " ".join(s)

    # better method

    def reverseWords(self, s: str) -> str:
        words = []

        l,r=0,0
        while r < len(s):
            
            mode = 'blank' if s[l]==' ' else 'word'
            
            if mode=='word':
                while r<len(s) and s[r]!=' ':
                    r+=1
                words.append(s[l:r])
                l=r
                
            l+=1
            r+=1
        return ' '.join(words[::-1])

