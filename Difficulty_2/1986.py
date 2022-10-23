# 1986. 지그재그 숫자
# 2022-10-23 (일)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nSum = 0 # nSum : 1부터 n까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값

    for x in range(1, n + 1):
        if x % 2 == 0: # (1) x가 짝수인 경우
            nSum -= x
        else: # (2) x가 홀수인 경우
            nSum += x
    
    print('#', test_case, ' ', nSum, sep = '')