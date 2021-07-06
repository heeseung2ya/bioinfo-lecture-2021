import sys


# 밑에 두 개를 합쳐서 쓰기!
try:
    val = int(input('Enter: '))
    print(10/val)
except ValueError as err:
    print(err)
    sys.exit(1)
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)





# 이 두 개를 합쳐서 쓰는 방법?
'''
try:
    val = int(input('Enter: '))
except ValueError as err:
    print(err)
    sys.exit(2)

try:
    print(10/val)
except ZeroDivisionError as err:
    print(err)
    sys.exit(1)
'''

