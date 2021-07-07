import sys

if len(sys.argv) != 2:
    print(f"#usage: python  {sys.argv[0]} [num]")
    sys.exit()


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


print(factorial(int(sys.argv[1])))
