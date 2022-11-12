# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
# 2022-11-12 (토)

import math

T = 10

for test_case in range(1, T + 1):
    test_num = int(input()) # test_num : 테스트 케이스의 번호
    n, m = map(int, input().split())

    print('#', test_case, ' ', int(math.pow(n, m)), sep = '')