""""
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n =len(strs)
        longest_common_prefix = []
        j=0
        if n>1:
            try:
                while j>=0:
                
                    letter=""
                    for i in range(len(strs)):
                        if not letter:
                            letter += strs[i][j]
                        
                        elif i==len(strs)-1:
                            new_letter = strs[i][j]
                            if new_letter==letter:
                                longest_common_prefix.append(letter)
                            else:
                                return ''.join(longest_common_prefix)
                        
                        else:
                            new_letter = strs[i][j]
                            if new_letter==letter:
                                pass
                            else:
                                return ''.join(longest_common_prefix) 
                    j+=1
            except:
                #when j in out of index range
                return ''.join(longest_common_prefix)
        else:
            return strs[0]  ## if there is only one word
            



        
            