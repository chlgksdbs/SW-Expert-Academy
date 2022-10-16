# 1983. 조교의 성적 매기기
# 2022-10-16 (일)

T = int(input())

for test_case in range(1, T + 1):
    # n : 학생의 수, k : 학점을 알고싶은 학생의 번호
    n, k = map(int, input().split())
    totalScore = [] # totalScore : 각각의 학생이 받은 시험 및 과제 점수를 비율에 따라 합한 총점
    kRank = 0 # kRank : 학점을 알고싶은 학생의 등수

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for num in range(1, n + 1):
        midScore, finalScore, projectScore = map(int, input().split())    
        totalScore.append([midScore * (0.35) + finalScore * (0.45) + projectScore * (0.2), num])
    
    totalScore.sort(key = lambda x : x[0], reverse = True) # 리스트의 첫 번째 원소를 기준으로 내림차순 정렬

    for i in range(n):
        if totalScore[i][1] == k:
            kRank = i
            break
    
    dn = n // 10 # dn : 학생의 수는 10의 배수이므로, n을 10으로 나누어 dn을 계산
    print('#', test_case, ' ', grade[kRank // dn], sep = '')