# 1289. 원재의 메모리 복구하기
# 2022-11-14 (월)

T = int(input())

for test_case in range(1, T + 1):
    orginalMemory = input() # orginalMemory : 메모리의 원래 값
    cnt = 0 # cnt : 초기값에서 원래 값으로 복구하기 위한 최소 수정 횟수
    currentValue = "0" # currentValue : 현재 메모리의 값

    for x in orginalMemory:
        if x != currentValue:
            cnt += 1
            if currentValue == "0":
                currentValue = "1"
            else:
                currentValue = "0"

    print('#', test_case, ' ', cnt, sep = '')