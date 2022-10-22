# 1970. 쉬운 거스름돈
# 2022-10-20 (목)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 손님에게 거슬러 주어야 할 금액
    coinTypes = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # coinTypes : 돈의 종류

    print('#', test_case, sep = '')
    for x in coinTypes:
        if n // x: # n 나누기 x가 0이 아닌 경우 (나누어질 수가 있는 경우)
            print((n // x), end = ' ')
            n %= x
        else:
            print(0, end = ' ')
    print()