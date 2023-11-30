#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    count = 0
    
    # methord 1
    # for i in range(max(a), min(b) + 1):
    #     count += (all([i % aa == 0 for aa in a]) and all([bb % i == 0 for bb in b]))
    # return count
    
    # methord 2
    for i in range(max(a), min(b) + 1):
        is_common_factor_of_a = True
        for aa in a:
            if i % aa != 0:
                is_common_factor_of_a = False
                break
                
        is_factor_of_b = True
        for bb in b:
            if bb % i != 0:
                is_factor_of_b = False
                break
        if is_common_factor_of_a and is_factor_of_b:
            count += 1
    
    return count
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()