# 1984. 중간 평균값 구하기
# 2022-10-23 (일)

T = int(input())

for test_case in range(1, T + 1):
    # numList : 10개의 수
    numList = list(map(int, input().split()))
    average = 0 # numList의 최대 수와 최소 수를 제외한 평균 값

    maxNum = max(numList) # maxNum : numList의 최대 수
    minNum = min(numList) # minNum : numList의 최소 수

    for x in numList:
        # x가 최대 수이거나 최소 수인 경우 if문 이하 생략
        if x == maxNum or x == minNum:
            continue
        average += x
    
    average = round(average / 8) # 2개의 수를 제외한 8로 나누어 평균 계산

    print('#', test_case, ' ', average, sep = '')