# 재귀 알고리즘으로 5! 구하는 프로그램


# def factorial(num, result):
#     if num < 1:
#         return result
#     result *= num
#     return factorial(num - 1, result)


# num = int(input("수를 입력하세요: "))
# result = 1
# result = factorial(num, result)

# print(result)


def factorial(num, result):
    if num == 1:
        return result
    result *= num
    return factorial(num - 1, result)


result = 1
num = int(input("Enter: "))
final_result = factorial(num, result)
print(final_result)

# f(5) = (1 *) 5 * 4 * 3 * 2 * 1


