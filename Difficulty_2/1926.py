# 1926. 간단한 369게임
# 2022-10-09 (일)

n = int(input())

for i in range(1, n + 1):
    nStr = str(i)
    minusStr = '' # minusStr : '-'를 담는 문자열
    n_flags = 0 # n_flags : nStr에 3, 6, 9의 숫자가 있는 경우 1, 아닌 경우 0

    for x in nStr:
        if int(x) != 0 and int(x) % 3 == 0:
            minusStr += '-'
            n_flags = 1
    
    if n_flags == 0:
        print(int(i), end = ' ')
    else:
        print(minusStr, end = ' ')
