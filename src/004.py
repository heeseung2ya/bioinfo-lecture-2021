# if-else

import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()

num = int(sys.argv[1])

if num % 2 == 0:
    print('even')
else:
    print('odd')


'''
# 이렇게 하면 else를 사용하지 않고도 같은 결과를 낼 수 있다.
result = 'odd'
if num % 2 == 0:
    result = 'even'
print(result)
'''
