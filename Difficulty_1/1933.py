# 1933. 간단한 N 의 약수
# 2022-10-20 (목)

n = int(input())

for i in range(1, n + 1):
    if n % i == 0: # n이 i로 나누어 떨어지는 경우, i는 n의 약수이다.
        print(i, end = ' ')