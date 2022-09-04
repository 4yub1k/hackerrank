"""
https://www.hackerrank.com/challenges/apple-and-orange/problem

Itertools : https://docs.python.org/3/library/itertools.html#itertools.zip_longest
"""


# zip_longest will by default fill unequal list value with None, and you can custom <fill fillvalue=0>
# it is similar to zip but can handle [1, 2, 3], [4, 5] = [1,4], [2, 5], [3, None]
from itertools import zip_longest

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

# Short #################################################################
def countApplesAndOranges(s, t, a, b, apples=None, oranges=None):
    
    fruits: dict = {"apple":0, "orange":0}

    for apple, orange in zip_longest(apples, oranges, fillvalue=0):

        pos_apple = a + apple
        if pos_apple >= s and pos_apple <= t and apple != 0:
            fruits["apple"] += 1     # use setdefault if key not there
        
        pos_orange = b + orange
        if pos_orange >= s and pos_orange <= t and orange != 0:
            fruits["orange"] += 1     # use setdefault if key not there
            
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


# Detailed #################################################################
def countApplesAndOranges(s, t, a, b, apples=None, oranges=None):
   
    fruits: dict = {"apple":0, "orange":0}

    for dist_apple in apples: # dist_apple = distance of apple from a (apple tree)
        position = a + dist_apple
        if position >= s and position <= t:
            fruits["apple"] += 1     # use setdefault if key not there
    
    for dist_orange in oranges: # dist_orange = distance of orange b (orange tree)
        position = b + dist_orange
        if position >= s and position <= t:
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
