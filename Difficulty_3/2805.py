# 2805. 농작물 수확하기
# 2022-10-14 (금)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 농장의 크기
    graph = [] # graph : 농장
    answer = 0 # answer : 규칙에 따라 얻을 수 있는 수익

    for _ in range(n):
        graph.append(list(map(int, input())))

    mid = n // 2 # mid : 리스트 원소의 중간 인덱스 부분
    end = len(graph) - 1 # end : 리스트 원소의 끝 인덱스 부분
    
    for i in range(mid): # graph의 가운데를 제외한 위, 아래 리스트 값 더하기
        for j in range(i + 1):
            if j == 0: # j가 0인 경우 가운데 농장 데이터만 더하기
                answer += graph[i][mid] # 위
                answer += graph[end - i][mid] # 아래
            else: # j가 0이 아닌 경우 가운데를 기준으로 왼쪽, 오른쪽 데이터 더하기
                answer += graph[i][mid - j] + graph[i][mid + j] # 위
                answer += graph[end - i][mid - j] + graph[end - i][mid + j] # 아래
    
    for i in range(n): # graph의 가운데 리스트 값 더하기
        answer += graph[mid][i]

    print('#', test_case, ' ', answer, sep = '')