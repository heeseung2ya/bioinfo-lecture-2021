# 
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)

num = int(sys.argv[1])

try:
    res = 10 / num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)

print(res)

'''

# echo $? 를 통해 sys.exit() 의 코드를 알 수 있음.
# 어디서 오류가 났는지!

'''
