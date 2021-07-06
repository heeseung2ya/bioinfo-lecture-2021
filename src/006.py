# for
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()

num = int(sys.argv[1])
result = 0

for i in range(1, num+1):
    result += i

print(result)
