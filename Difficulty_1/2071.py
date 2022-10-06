# 2071. 평균값 구하기
# 2022-10-06 (목)

T = int(input())

for test_case in range(1, T + 1):
    # nList : 10개의 정수를 담는 리스트
    nList = list(map(int, input().split()))

    result = round(sum(nList) / 10) # 10개의 수의 평균값을 계산하고 소수점 첫째 자리에서 반올림
    
    print('#', test_case, ' ', result, sep = '')