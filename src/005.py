# if-elif-else
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0] [num]}')
    sys.exit()

num = int(sys.argv[1])

if num % 3 == 0 and num % 7 == 0:
    print('3과 7의 배수')
elif num % 3 == 0:
    print('3의 배수')
elif num % 7 == 0:
    print('7의 배수')


