"""
https://www.hackerrank.com/challenges/finding-the-percentage
"""

# short
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

print("{:.2f}".format(sum(student_marks[query_name]) / 3))


# Detail

# if __name__ == '__main__':
#     n = 3
#     student_marks = {
#         "Krishna": [67, 68, 69],
#         "Arjun": [70, 98, 63],
#         "Malika": [52, 56, 60],
#     }

#     query_name = "Malika"

# sum = 0

# for marks in student_marks[query_name]:
#     sum += marks

# average = sum / len(student_marks[query_name])

# print("%0.2f" % average)
