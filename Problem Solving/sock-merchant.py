"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(arr: list=None):
    
    sock_count: dict = {}
    count_: int = 0

    for sock in arr:
        
        if sock in arr:
            sock_count.setdefault(sock, 0)
            sock_count[sock] += 1

        if sock_count[sock]%2 == 0:
            count_ += 1

    # print(sock_count)
    # print(count)
    return count_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
