# while
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0] [num]}')
    sys.exit()

num = int(sys.argv[1])

i = 1
result = 1
while i <= num:
    result *= i
    i += 1

print(result)
