"""
https://www.hackerrank.com/contests/ieor-department-coding-test-2/challenges/crush/problem

difficulty : Hard
"""


# brute force
# time complexity O(m*(b-a)) 

def arrayManipulation(n, queries):
  dic = {}

  for i in range(1,n+1):
    dic[i]=0
    
  for a,b,k in queries:
    idx=a
    while idx<=b:
      dic[idx]+=k

return max(dic.values())

#_____________________________________________

## prefix sum
# time complexity O(m+n)

def arrayManipulation(n, queries):
    # Write your code here
    arr=[0]* (n+2)
    
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1] -=k
    
    max_sum= temp_sum =0
    
    for val in arr:
        temp_sum+=val  #prefix sum
        max_sum = max(max_sum,temp_sum)
    
    return max_sum
