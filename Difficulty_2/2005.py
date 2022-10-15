# 2005. 파스칼의 삼각형
# 2022-10-15 (토)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 파스칼 삼각형의 크기
    graph = [[] for _ in range(n)] # graph : 파스칼 삼각형

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                graph[i].append(1)
            else:
                # 왼쪽과 오른쪽 위의 숫자의 합
                graph[i].append(graph[i - 1][j - 1] + graph[i - 1][j])

    print('#', test_case, sep = '')
    for i in range(n):
        for j in range(len(graph[i])):
            print(graph[i][j], end = ' ')
        print()