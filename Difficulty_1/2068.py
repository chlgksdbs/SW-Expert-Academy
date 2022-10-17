# 2068. 최대수 구하기
# 2022-10-18 (화)

T = int(input())

for test_case in range(1, T + 1):
    numList = list(map(int, input().split())) # numList : 10개의 수를 담은 리스트

    print('#', test_case, ' ', max(numList), sep = '')