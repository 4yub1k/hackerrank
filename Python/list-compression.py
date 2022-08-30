"""
Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.
Please use list comprehensions rather than multiple loops, as a learning exercise.

input :
1
1
1
2

ouput :
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
# Summary : 
# just run 3 nested for loops, from 0 to the given number.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
# like  binary, simple range
for i in range(x + 1):
    for j in range(y +1):
        for k in range(z + 1): 
            if (i + j + k) != n:
                print(i, j, k)

# List compression
result =[[i,j,k] for i in range(x + 1) for j in range(y +1) for k in range(z + 1)
        if (i + j + k) != n]

print(result)
