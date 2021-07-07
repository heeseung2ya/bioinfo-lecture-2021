# 함수에 값 전달

import sys

if len(sys.argv) != 3:
    print(f"#usage: python  {sys.argv[0]} [num1] [num2]")
    sys.exit()


def mySum(x, y):
    print(x + y)


mySum(int(sys.argv[1]), int(sys.argv[2]))
