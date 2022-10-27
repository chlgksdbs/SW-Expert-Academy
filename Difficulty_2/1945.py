# 1945. 간단한 소인수분해
# 2022-10-27 (목)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nList = [11, 7, 5, 3, 2] # nList : n의 약수들의 집합
    answer = []
    for x in nList:
        if n % x == 0:
            cnt = 0
            while True:
                if n % x == 0:
                    cnt += 1
                    n //= x
                else:
                    break
            answer.append(cnt)
        else:
            answer.append(0)
    answer.reverse()
    print('#', test_case, ' ', sep = '', end = '')
    for x in answer:
        print(x, end = ' ')
    print()