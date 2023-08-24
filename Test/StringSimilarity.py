"""
String Similarity
difficulty--> hard

For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example, the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

Sample Input

2
ababaa  
aa
Sample Output

11  
3
Explanation

For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", "baa", "aa" and "a". The similarities of these strings with the string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is 6 + 0 + 3 + 0 + 1 + 1 = 11.

https://www.hackerrank.com/contests/coding-test-1-1692470130/challenges/string-similarity/problem
"""

def calculate_z_array(string):
    n = len(string)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def stringSimilarity(string):
    z_array = calculate_z_array(string)
    similarity_sum = len(string)  # Include the length of the original string
    
    for lcp in z_array:
        similarity_sum += lcp
    
    return similarity_sum