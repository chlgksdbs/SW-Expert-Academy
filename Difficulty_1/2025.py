# 2025. N줄덧셈
# 2022-10-22 (토)

n = int(input())
nSum = 0 # nSum : 1 ~ n까지의 덧셈을 저장하는 변수

for x in range(1, n + 1):
    nSum += x

print(nSum)