# 1948. 날짜 계산기
# 2022-11-01 (화)

T = int(input())

for test_case in range(1, T + 1):
    # m1, d1 : 1번째 월/일, m2, d2 : 2번째 월/일
    m1, d1, m2, d2 = map(int, input().split())

    dayList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # dayList : 1월부터 12월까지의 일 수 리스트
    firstDay = 0
    secondDay = 0

    for i in range(1, m1):
        firstDay += dayList[i]
    firstDay += d1
    for i in range(1, m2):
        secondDay += dayList[i]
    secondDay += d2

    print('#', test_case, ' ', (secondDay - firstDay + 1), sep = '')