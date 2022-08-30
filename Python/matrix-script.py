"""
Neo has a complex matrix script. The matrix script is a  N x M  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&)

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. 
Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

"""

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matchdict = {'code':''}

for j in range(m):
    for i in matrix:
        matchdict["code"] += i[j]

regex = r"[a-zA-z0-9][!@#$%&\s]+[a-zA-z0-9]"
reg = re.finditer(regex, matchdict["code"])

for i in reg:
    matchdict[i.end()-1] = [i.start()+2, i.end()-1] #for reverse use

new_string = list(matchdict["code"][::-1]) # reverse code, convert to list, as strins are immutable

for index in range (-len(matchdict["code"]), 0, 1): # -size to -1
    try:
        new_string[-matchdict[-index][1]:-matchdict[-index][0]+1] = " "
    except KeyError:
        pass

print(*new_string[::-1], sep="")    # sep="" remove spaces when showing output
