# 2001. 파리 퇴치
# 2022-10-10 (월)

T = int(input())

for test_case in range(1, T + 1):
    answer = 0 # answer : 죽은 파리의 수
    # n : 파리가 존재하는 영역의 크기, m : 파리채의 크기
    n, m = map(int, input().split())
    graph = [] # graph : 파리가 존재하는 영역

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            tempNum = 0 # tempNum : m x m 크기의 파리채 공간의 파리의 수
            for x in range(i, i + m):
                for y in range(j, j + m):
                    tempNum += graph[x][y]

            if answer < tempNum: # 최댓값 갱신
                answer = tempNum

    print('#', test_case, ' ', answer, sep = '')