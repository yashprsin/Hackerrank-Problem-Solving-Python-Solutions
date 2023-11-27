#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = sum([1 for x in arr if x > 0])
    neg = sum([1 for x in arr if x < 0])
    neu = sum([1 for x in arr if x == 0])

    total = len(arr)

    print(pos/total)
    print(neg/total)
    print(neu/total)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
