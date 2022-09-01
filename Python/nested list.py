"""
https://www.hackerrank.com/challenges/nested-list
"""

# Easy Way, Usgin everything builtin

# if __name__ == '__main__':
#     score_list = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         score_list.append([name, score])

#     second_highest = sorted(set([score for name, score in score_list]))[1]
#     print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))


#-----------------------------------------------------------------------------------------------------
# Detail way

def bubble_sort(students=None, sort_by=0):

    # 0 - sort by numbers, 1 - sort by names
    size = len(students)
    
    for i in range(size):
        for j in range(size - i -1):
            # Change <, > to change sorting order!
            # Sort on values bases, and save on index bases
            if sort_by == 0:
                if students[j][1] < students[j + 1][1]: 
                    students[j], students[j+1] = students[j+1], students[j]
            # students[0][0] = "Harry", students[0][0][:1] = 'H'
            # alpha order , A < B = True, B < A = False
            # ord('A') = 65, ord('B') = 66, it will compare decimal value
            # And make all first letter lowercase or capital case
            if sort_by == 1:
                if str.lower(students[j][0][:1]) > str.lower(students[j + 1][0][:1]):
                    students[j], students[j+1] = students[j+1], students[j]
            
            if sort_by == 2:
                if students[j] < students[j + 1]: 
                    students[j], students[j+1] = students[j+1], students[j]
    
    return students

def remove_same_value(students):
    
    # You can use sets, or list with check not in list, set also takes iterables, list compression
    student = []
    for _, value in students:
        if value not in student:
            student.append(value)
    return student 

def find_second_lowest(students, students_second_lowest):

    students_lowest = []
    for name, value in students:
        if value == students_second_lowest[-2]: # [41, 39, 37.21, 37.2][-2] = 2, second lowest after sorting
            students_lowest.append([name, value])

    return students_lowest

if __name__ == "__main__":
    """input

    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    """
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    # 0 - sort by numbers, 1 - sort by names, 2 - for simple list [2, 3, 5, 2, 1]

    # Marks wise
    no_duplicate = remove_same_value(students)
    students_lowest = bubble_sort(no_duplicate, sort_by=2)

    # Name wise
    students_2 = find_second_lowest(students, students_lowest)
    students_lowest = bubble_sort(students_2, sort_by=1)

    print(*[name[0] for name in students_lowest], sep="\n")
    # students = find_second_lowest(students)
    # students = bubble_sort(students, sort_by=0)


# TestCase 
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21

# Beria
# Harsh
