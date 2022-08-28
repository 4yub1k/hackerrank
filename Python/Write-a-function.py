"""
1- The year must be evenly divisible by 4;
2- If the year can also be evenly divided by 100, it is not a leap year;
  unless...
3- The year is also evenly divisible by 400. Then it is a leap year.
"""

# SOLUTION 1:
def is_leap(year):
    leap = False

    #Must be divisble by 4
    if year%4 == 0:
        # If divisble by 100, then also be divisble by 400
        if year%100 == 0 and year%400 == 0:
            leap = True
        # Or only divible by 4
        if year%100 != 0 and year%400 != 0:
            leap = True
                
    return leap

year = int(input())
print(is_leap(year))

# SOLUTION 2:

def is_leap(year):
    leap = False

    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
