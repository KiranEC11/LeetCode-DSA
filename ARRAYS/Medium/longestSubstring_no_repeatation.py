"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""

# Brute Force

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        count=0
        max_length=0
        n = len(s)
        for i in range(n):
            count =1
            charset.add(s[i])
            for j in range(i+1,n):
                if s[j] not in charset:
                    count+=1
                    charset.add(s[j])
                else:
                    break
            charset=set()
            if count>max_length:
                max_length = count 
        return max_length
                    

## another brute force
# O(n3)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        main_count = 0
        
        n = len(s)
        i=0
        while i < n-main_count:
            j = i+1
            
            count=1  # min length is one --> I have already append s[i] in the substring 
            while j< n and s[j] not in s[i:j]:
                count +=1
                j+=1
            if count > main_count:
                main_count = count
            
            i+=1
        return main_count
                    

## Efficient approach
# window search
# O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        left = 0
        char_index = {}  # key = char and values = index

        main_count = 0
        count=0
        for right in range(len(s)):
            if s[right] in char_index:
                if char_index[s[right]] >= left and char_index[s[right]] < right:
                    # old_left = left
                    left = char_index[s[right]] + 1
                    
            char_index[s[right]] = right
            count = right - left + 1
            if count > main_count:
                main_count = count
                    
        return main_count




                    
            
                
         
                
