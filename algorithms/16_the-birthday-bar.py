#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    
    # ti=0
    # for x in range(0,len(s)):
    #     t=0
    #     # print(t)
    #     for y in range(x,x+m):
    #         try:
    #             t=t+s[y]
    #         except:
    #             pass
    #     if (t == d):
    #         ti+=1
    # return ti
    
    ans = 0
    for i in range(len(s)):
        n=0
        count=0
        while(n<(m)):
            count += s[i+n]
            n+=1
        if count==d:
            ans+=1
        if (n+i==len(s)):
            break
    return ans
    # for i in range(len(s)):
    #     n=0
    #     count=0
    #     while(n<(m)):
    #         count+=s[i+n]
    #         n+=1
    #         if(count==d):
    #             ti+=1
    #         if(i+n==len(s)):
    #             break
    #     return ti

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
