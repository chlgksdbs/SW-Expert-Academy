# 1959. 두 개의 숫자열
# 2022-10-16 (일)

T = int(input())

for test_case in range(1, T + 1):
    # n : aList의 크기, m : bList의 크기
    n, m = map(int, input().split())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    answer = 0 # answer : 서로 마주보는 숫자들의 곱 중 최댓값

    if len(aList) < len(bList):
        lenAB = len(bList) - len(aList) # lenAB : aList와 bList의 크기 차이
        for i in range(lenAB + 1):
            tempSum = 0 # tempSum : 서로 마주보는 숫자들의 곱
            for j in range(len(aList)):
                tempSum += aList[j] * bList[i + j]
            if answer < tempSum:
                answer = tempSum

    else:
        lenAB = len(aList) - len(bList)
        for i in range(lenAB + 1):
            tempSum = 0
            for j in range(len(bList)):
                tempSum += bList[j] * aList[i + j]
            if answer < tempSum:
                answer = tempSum

    print('#', test_case, ' ', answer, sep = '')