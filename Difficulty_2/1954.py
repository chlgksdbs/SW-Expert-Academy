# 1954. 달팽이 숫자
# 2022-10-05 (수)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 달팽이의 크기
    nSize = n * n # nSize : 반복문 실행횟수

    graph = [[0] * n for _ in range(n)]

    x = 0 # x : 행을 나타내는 인덱스
    y = 0 # y : 열을 나타내는 인덱스
    direct = 1 # direct : 방향을 나타내는 플래그 값 (1 : 동쪽, 2 : 남쪽, 3 : 서쪽, 4 : 북쪽)
    
    for num in range(1, nSize + 1):
        graph[x][y] = num
        
        # 방향에 따른 좌표 이동
        if direct == 1:
            if (y + 1) <= (n - 1) and graph[x][y + 1] == 0:
                y += 1
            else:
                x += 1
                direct = 2
        elif direct == 2:
            if (x + 1) <= (n - 1) and graph[x + 1][y] == 0:
                x += 1
            else:
                y -= 1
                direct = 3
        elif direct == 3:
            if (y - 1) >= 0 and graph[x][y - 1] == 0:
                y -= 1
            else:
                x -= 1
                direct = 4
        else:
            if (x - 1) >= 0 and graph[x - 1][y] == 0:
                x -= 1
            else:
                y += 1
                direct = 1
    
    print('#', test_case, sep = '')
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end = ' ')
        print() # 줄바꿈을 위한 print문