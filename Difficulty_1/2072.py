# 2072. 홀수만 더하기
# 2022-10-05 (수)

T = int(input()) # T : 테스트 케이스의 개수

for test_case in range(1, T):
    numList = list(map(int, input().split())) # numList : 10개의 수
    numSum = 0 # numSum : 홀수의 합

    for x in numList:
        if x % 2 == 1: # 2로 나누었을 때 나머지가 1인 경우, 즉 홀수인 경우 numSum에 더하여 저장
            numSum += x
    
    print('#', test_case, ' ', numSum, sep = '')