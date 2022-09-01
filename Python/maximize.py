"""
https://www.hackerrank.com/challenges/maximize-it
"""

from itertools import product

def main():

    input_lists = []
    combinations_list = []
    solution = []   # Save final equation

    # Split the input at <space>, strip()
    list_numbers, mod = map(int, input().strip().split( " ")) # Either use loop, seperate input, or map to convert type

    while (list_numbers):
        # input value, convert datatype, insert in list
        # we don't need first element as it represents elements in list
        # 5 5 7 8 9 10, the first 5 is number of elements 5, 5, 7, 8, 9, 10
        input_lists.append(list(map(int, input().strip().split(" ")))[1:]) # [1:] slice list
        list_numbers -= 1

    # Finding combinations using itertools, 
    # [] is just a literal, while list() is a function, remember.
    # Cartesian product of lists.
    # https://note.nkmk.me/en/python-itertools-product/
    # https://stackoverflow.com/questions/3034014/how-to-apply-itertools-product-to-elements-of-a-list-of-lists
    
    combinations_list = list(product(*input_lists)) # anotherway is to use nested loops.

    for list_ in combinations_list:
        # you can use list unpacking or just print inside list
        sum_values_mod = sum(map(lambda x: x**2, list_)) % mod
        solution.append(sum_values_mod)

    return max(solution)

if __name__ == "__main__":
    print(main())
