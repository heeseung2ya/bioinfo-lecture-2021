from ValueCalculator import ValueCalculator
# 만약 ValueCalculator.py 안에 class가 여러 개 들어 있는데, 여러 개의 class를 improt 하고싶을 경우, 
# 이렇게 하면 모든 class를 다 불러오는데, 강사님은 추천하지 않는다고 하심.
# 어떤 class 요소를 불러오는지 명시가 안돼있어서 모르기 때문.
from ValueCalculator import *
from ValueCalculator import A, B, C # 이런 식으로 써도 됨.

value_calculator_1 = ValueCalculator("a")
value_calculator_2 = ValueCalculator("b")

res = value_calculator_1 + value_calculator_2
print(res)
