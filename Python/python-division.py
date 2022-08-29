"""
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
"""

# 1
class SimpleMath(object):
    
    @classmethod
    def floor_value(cls, a, b):
        return a//b
    
    @classmethod
    def div_value(cls, a, b):
        return a/b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(SimpleMath.floor_value(a, b))
    print(SimpleMath.div_value(a, b))    

# 2
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a//b)
    print(a/b)
