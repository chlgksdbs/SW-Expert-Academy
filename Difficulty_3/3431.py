# 3431. 준환이의 운동관리
# 2022-11-13 (일)

T = int(input())

for test_case in range(1, T + 1):
    # L, U : 준환이가 1주일에 해야 하는 운동의 기준치 (L : 시작(분), U : 종료(분)), X : 준환이가 한 운동 시간
    L, U, X = map(int, input().split())

    if L <= X and X <= U:
        print('#', test_case, ' ', 0, sep = '')
    elif X <= L:
        print('#', test_case, ' ', L - X, sep = '')
    else:
        print('#', test_case, ' ', -1, sep = '')