# 1961. 숫자 배열 회전
# 2022-11-05 (토)

# 90도 회전하는 함수
def rotate_degree_90(graph, graphSize):
    tempGraph = [[0] * graphSize for _ in range(graphSize)] # tempGraph : graph의 90도 회전한 모양을 담을 리스트

    for i in range(graphSize):
        for j in range(graphSize):
            tempGraph[i][j] = graph[graphSize - 1 - j][i]

    return tempGraph

# 180도 회전하는 함수
def rotate_degree_180(graph, graphSize):
    tempGraph = [[0] * graphSize for _ in range(graphSize)] # tempGraph : graph의 180도 회전한 모양을 담을 리스트

    for i in range(graphSize):
        for j in range(graphSize):
            tempGraph[i][j] = graph[graphSize - 1 - i][graphSize - 1 - j]

    return tempGraph

# 270도 회전하는 함수
def rotate_degree_270(graph, graphSize):
    tempGraph = [[0] * graphSize for _ in range(graphSize)] # tempGraph : graph의 270도 회전한 모양을 담을 리스트

    for i in range(graphSize):
        for j in range(graphSize):
            tempGraph[i][j] = graph[j][graphSize - 1 - i]

    return tempGraph

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 행렬의 크기
    graph = []

    # n x n 크기의 행렬 입력
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    newGraph1 = rotate_degree_90(graph, n)
    newGraph2 = rotate_degree_180(graph, n)
    newGraph3 = rotate_degree_270(graph, n)

    print('#', test_case, sep = '')

    for i in range(n):
        for j in range(n):
            print(newGraph1[i][j], end = '')
        print(end = ' ')
        
        for j in range(n):
            print(newGraph2[i][j], end = '')
        print(end = ' ')
        
        for j in range(n):
            print(newGraph3[i][j], end = '')
        print()