# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# 2022-10-06 (목)

T = int(input())

for test_case in range(1, T + 1):
    modeNum = [0] * 101 # modeNum : 최빈수를 계산하기 위한 리스트

    n = int(input()) # n : 테스트 케이스의 번호
    score = list(map(int, input().split())) # score : 1000명의 수학 성적

    for x in score:
        modeNum[x] += 1 # 해당 점수의 인덱스의 1을 count
    
    answer = 0 # answer : 가장 여러 번 나타나는 점수 값
    maxValue = max(modeNum) # maxValue : modeNum에서 가장 큰 값

    for i in range(len(modeNum)):
        if modeNum[i] == maxValue:
            answer = i
    
    print('#', test_case, ' ', answer, sep = '')