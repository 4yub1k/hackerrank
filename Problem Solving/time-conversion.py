"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""

def timeConversion(s):
    
    s = s.split(":")

    if s[-1].endswith("AM"):
        if s[0] == '12':
            hour = format(12 - int(s[0]), "02d")
        else:
            hour = format(int(s[0]), "02d")
        return "{}:{}:{}".format(hour, s[1], s[2][:-2] )
    else:
        if s[0] == '12':
            hour = format(int(s[0]), "02d")
        else:
            hour = format(12 + int(s[0]), "02d")
        return "{}:{}:{}".format(hour, s[1], s[2][:-2] )

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
