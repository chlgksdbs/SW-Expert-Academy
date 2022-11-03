# 1966. 숫자를 정렬하자
# 2022-11-03 (목)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    numList = list(map(int, input().split()))

    numList.sort() # 오름차순 정렬

    print('#', test_case, sep = '', end = ' ')
    
    for x in numList:
        print(x, end = ' ')
    print()