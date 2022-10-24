# 1859. 백만 장자 프로젝트
# 2022-10-25 (화)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 물건 판매의 기간
    price = list(map(int, input().split())) # price : 각 날의 매매가
    result = 0 # result : 사재기를 통해 이득을 본 금액
    buyCount = 0 # buyCount : 물건을 구입한 개수
    
    maxPrice = max(price[:]) # maxPrice : price 리스트 중 최댓값
    for i in range(n):
        if price[i] == maxPrice: # index가 i일때의 price값이 maxPrice 값인 경우
            result += buyCount * maxPrice # buyCount만큼 크기를 현재 매매가로 판매 (덧셈)
            buyCount = 0
            if i != n - 1:
                maxPrice = max(price[(i + 1):]) # 나머지 리스트 값 중의 최댓값으로 maxPrice를 갱신
        else: # 현재 price값이 maxPrice 값이 아닌 경우
            result -= price[i] # 현재 price(매매가)를 구입 (뺄셈)
            buyCount += 1
    
    print('#', test_case, ' ', result, sep = '')

'''
T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 물건 판매의 기간
    price = list(map(int, input().split()))[::-1] # price : 각 날의 매매가 (입력의 역순으로 리스트 생성)
    result = 0 # result : 사재기를 통해 이득을 본 금액
    maxValue = price[0] # maxValue : 시작 값을 최댓값으로 설정

    for i in range(1, n):
        if price[i] >= maxValue: # 현재값이 maxValue 값보다 큰 경우 최댓값 갱신
            maxValue = price[i]
        else: # 현재값이 maxValue보다 작은 경우 차익을 result에 더함
            result += maxValue - price[i]
    
    print('#', test_case, ' ', result, sep = '')
'''