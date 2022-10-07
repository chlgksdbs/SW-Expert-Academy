# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# 2022-10-07 (금)

T = 10

for test_case in range(1, T + 1):
    dumpCount = int(input()) # dumpCount : 덤프 횟수
    box = list(map(int, input().split())) # box : 각 상자의 높이 정보

    for _ in range(dumpCount):
        maxValue = max(box) # box의 최댓값
        minValue = min(box) # box의 최솟값

        # 덤프 수행
        for i in range(len(box)):
            if box[i] == minValue:
                box[i] += 1
                break
        for i in range(len(box)):
            if box[i] == maxValue:
                box[i] -= 1
                break

    print('#', test_case, ' ', (max(box) - min(box)), sep = '')