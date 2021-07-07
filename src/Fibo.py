# l_fibo = [0, 1]
l_fibo = []
num = int(input("숫자를 입력하세요: "))

for i in range(num - 2):
    if len(l_fibo) == 0:
        l_fibo.append(0)
    elif len(l_fibo) == 1:
        l_fibo.append(1)
    else:
        l_fibo.append(l_fibo[-1] + l_fibo[-2])

print(l_fibo)
