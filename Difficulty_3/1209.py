# 1209. [S/W 문제해결 기본] 2일차 - Sum
# 2022-10-16 (일)

T = 10

for test_case in range(1, T + 1):
    n = int(input()) # n : 테스트 케이스의 번호
    graph = [] # graph : 100 x 100 크기의 2차원 리스트
    for _ in range(100):
        graph.append(list(map(int, input().split())))
    
    maxSum = 0 # maxSum : 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값

    for i in range(100): # 행의 합 중 최댓값 계산
        columnSum = sum(graph[i])
        if maxSum < columnSum:
            maxSum = columnSum

    for i in range(100): # 열의 합 중 최댓값 계산
        rowSum = 0
        for j in range(100):
            rowSum += graph[j][i]
        
        if maxSum < rowSum:
            maxSum = rowSum
    
    rightDiagonalSum = 0 # rightDiagonalSum : 오른쪽 방향의 대각선의 합
    leftDiagonalSum = 0 # leftDiagonalSum : 왼쪽 방향의 대각선의 합
    for i in range(100): # 대각선의 합 중 최댓값 계산
        rightDiagonalSum += graph[i][i]
        leftDiagonalSum += graph[i][99 - i]
    
    if maxSum < max(rightDiagonalSum, leftDiagonalSum):
        maxSum = max(rightDiagonalSum, leftDiagonalSum)
    
    print('#', test_case, ' ', maxSum, sep = '')
    