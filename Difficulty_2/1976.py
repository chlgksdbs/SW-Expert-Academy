# 1976. 시각 덧셈
# 2022-11-04 (금)

T = int(input())

for test_case in range(1, T + 1):
    # h1, h2 : 시, m1, m2 : 분
    h1, m1, h2, m2 = map(int, input().split())

    totalH = h1 + h2
    totalM = m1 + m2

    if totalM >= 60: # m1과 m2의 합이 60보다 크거나 같은 경우
        temp = totalM // 60
        totalM %= 60
        totalH += temp
    
    if totalH > 12: # h1과 h2의 합에 위 조건문에서의 temp값을 더한 값이 12보다 큰 경우
        if totalH % 12 == 0:
            totalH = 12
        else:
            totalH %= 12

    print('#', test_case, ' ', totalH, ' ', totalM, sep = '')