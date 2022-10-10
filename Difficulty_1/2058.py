# 2058. 자릿수 더하기
# 2022-10-10 (월)

n = input() # n : 자연수
nSum = 0 # nSum : 각 자릿수의 합

for x in n:
    nSum += int(x)

print(nSum)