# 1206. [S/W 문제해결 기본] 1일차 - View
# 2022-10-05 (수)

T = 10

for test_case in range(1, T + 1):
    n = int(input()) # n : 건물의 개수
    height = list(map(int, input().split())) # height : n개의 건물의 높이
    result = 0 # result : 조망권이 확보된 세대의 수

    for i in range(2, len(height) - 2):
        
        # 좌우로 2칸에서 건물의 최대 높이
        max_height = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        
        if height[i] - max_height >= 0: # 조망권이 확보된 세대의 경우
            result += height[i] - max_height

    print('#', test_case, ' ', result, sep ='')