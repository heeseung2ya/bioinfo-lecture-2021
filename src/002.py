# 반지름을 나타내는 변수 r을 사용하여 원의 넓이를 구해봅시다.

import math
import sys

if len(sys.argv) != 2:
    print(f'#usage: python  {sys.argv[0]} [num]')
    sys.exit()

r = int(sys.argv[1])
#r = int(input('반지름을 입력하세요: '))
result = (r ** 2) * 3.14
# pi = math.pi 로 pi를 가져올 수도 있다.

print(result)
