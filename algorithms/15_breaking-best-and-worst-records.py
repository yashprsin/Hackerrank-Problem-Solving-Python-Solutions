#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score, min_score_ls, max_score, max_score_ls = 0, scores[0], 0, scores[0]
    for i in scores:
        if i > max_score_ls:
            max_score_ls = i
            max_score += 1
        elif i < min_score_ls:
            min_score_ls = i
            min_score += 1
    return max_score, min_score
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
