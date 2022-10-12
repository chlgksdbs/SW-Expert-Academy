# 2070. 큰 놈, 작은 놈, 같은 놈
# 2022-10-12 (수)

T = int(input())

for test_case in range(1, T + 1):
    num1, num2 = map(int, input().split())

    if num1 > num2:
        print("#", test_case, ' ', ">", sep = '')
    elif num1 == num2:
        print("#", test_case, ' ', "=", sep = '')
    else:
        print("#", test_case, ' ', "<", sep = '')