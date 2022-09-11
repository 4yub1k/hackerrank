"""
https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def julian_leap(year):

    leap = False

    if year%4 == 0:
        leap = True

    if leap:
        m = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
    else:
        m = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31

    d = 256 - m

    return leap, date_string(d, 9, year)

def geo_leap(year):

    leap = False

    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True

    if leap:
        m = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
    else:
        m = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31

    d = 256 - m

    return leap, date_string(d, 9, year) 

def date_string(d, m, year):
    return '{0:02g}.{1:02g}.{2}'.format(d , 9, year)

def dayOfProgrammer(year):
    
    if year == 1918:
        # when the next day after January 31st was February 14th
        m = 31 + 15 + 31 + 30 + 31 + 30 + 31 + 31
        d = 256 - m
        return date_string(d, 9, year)
    
    elif year >= 1918:
        #print("Jul %d %s" % (year, geo_leap(year)))
        return geo_leap(year)[1]
    
    else:
        #print("Geo %d %s" % (year, julian_leap(year)))
        return julian_leap(year)[1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
