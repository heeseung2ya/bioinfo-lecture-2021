# n을 입력받아 10 / n 을 출력하는 프로그램
# n == 0 인 경우, try-except 로 잡기.

n = int(input("10을 몇으로 나눌까요?: "))

try:
    print(10 / n)
except ZeroDivisionError as err:
    print(f"{err}: 0으로 나눌 수 없습니다!")

