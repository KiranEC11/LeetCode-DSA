"""
https://www.hackerrank.com/contests/atc-test-1-coding/challenges/find-angle
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
c = float(input())
a =float(input())

import math

b = math.sqrt(c**2 + a**2)
# print(b)
# tanA = c/a
C = math.atan(c/a)  ## in radians
# print(math.degrees(C))
# print(C)
d =b/2
cc = math.sqrt(a**2 + d**2 - 2*a*d*math.cos(C))

D = math.asin((d/cc)*math.sin(C))  ## in radians
DD = math.degrees(D) ## degrees
# print(DD)
if DD>= int(DD)+0.5:
    angle = int(DD)+1 
    print(f"{angle}\u00B0")   #### unicode for degrees 
else:
    angle = int(DD)
    print(f"{angle}\u00B0")
