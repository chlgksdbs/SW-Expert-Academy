# 10505. 소득 불균형
# 2022-11-18 (금)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 사람의 수
    nList = list(map(int, input().split())) # nList : n명의 사람의 소득

    nAvg = 0 # nAvg : nList의 평균을 저장하는 변수

    for x in nList:
        nAvg += x
    nAvg //= n

    nCount = 0 # nCount : 평균 이하의 소득을 가진 사람들의 수

    for x in nList:
        if x <= nAvg:
            nCount += 1
    
    print('#', test_case, ' ', nCount, sep = '')
