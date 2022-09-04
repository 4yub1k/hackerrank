"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples=None, oranges=None):
  
    pos_apples = []
    pos_oranges = []
    fruits: dict = {"apple":0, "orange":0}

    for dist_apple in apples: # dist_apple = distance of apple from a (apple tree)
        position = a + dist_apple
        pos_apples.append(position)
    
    for pos_apple in pos_apples:
        if pos_apple >= s and pos_apple <= t:
            fruits["apple"] += 1     # use setdefault if key not there

    for dist_orange in oranges: # dist_orange = distance of orange b (orange tree)
        position = b + dist_orange
        pos_oranges.append(position)

    for pos_orange in pos_oranges:
        if pos_orange >= s and pos_orange <= t:
            fruits["orange"] += 1     # use setdefault if key not there

    # print(pos_apples, pos_oranges) # [3, 7, 6] [20, 9]
    print(*fruits.values(), sep="\n") # print with "\n" instead of whitespace
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
