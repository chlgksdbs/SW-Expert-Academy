# 5215. 햄버거 다이어트
# 2022-11-14 (월)

T = int(input())

for test_case in range(1, T + 1):
    # n : 재료의 수, l : 제한 칼로리
    n, l = map(int, input().split())
    v = [0] # v : 각 재료의 맛에 대한 점수 (0번째 인덱스는 0으로 초기화)
    w = [0] # w : 각 재료의 칼로리 (0번째 인덱스는 0으로 초기화)
    dp = [[0] * (l + 1) for _ in range(n + 1)] # dp : 2차원 dp 테이블 생성

    for _ in range(n):
        tempV, tempW = map(int, input().split())
        v.append(tempV)
        w.append(tempW)
    
    for i in range(1, n + 1): # i : i번째 재료
        for j in range(1, l + 1): # j : 현재 칼로리의 양
            if w[i] > j: # 재료의 칼로리가 현재 칼로리보다 큰 경우
                dp[i][j] = dp[i - 1][j] # 이전 값을 삽입
            else: # 재료의 칼로리가 현재 칼로리보다 작거나 같은 경우
                # (1) 이전의 값과 (2) 현재 칼로리 + 현재 칼로리를 뺀 이전의 값을 더한 칼로리 중 최댓값을 삽입
                dp[i][j] = max(dp[i - 1][j], v[i] + dp[i - 1][j - w[i]])
    
    print('#', test_case, ' ', dp[n][l], sep = '')
