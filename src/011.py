
def greet():
    print('Hello, Bioinformatics')

def greet1(name: str) -> None:
    print(f'Hello, {name}')

def greet2(num: int) -> int:
    return num * 2

greet()
ret1 = greet1('heeseung')
print(ret1)
# greet1 이라는 함수는 반환값(return)이 없기 때문에 print를 하더라도 아무 값이 없어서 None이라고 출력된다.

ret = greet2(3)
print(ret)


