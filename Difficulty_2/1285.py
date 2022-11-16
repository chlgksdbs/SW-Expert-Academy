# 1285. 아름이의 돌 던지기
# 2022-11-16 (수)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 돌을 던지는 사람의 수
    stoneLoc = list(map(int, input().split())) # stoneLoc : 각 사람이 돌을 던졌을 때 돌이 떨어진 위치

    for i in range(len(stoneLoc)):
        if stoneLoc[i] < 0:
            stoneLoc[i] = abs(stoneLoc[i])

    minValue = min(stoneLoc)
    minValueCount = stoneLoc.count(minValue)

    print('#', test_case, ' ', minValue, ' ', minValueCount, sep = '')
