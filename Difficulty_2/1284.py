# 1284. 수도 요금 경쟁
# 2022-10-24 (월)

T = int(input())

for test_case in range(1, T + 1):
    # [A사] p : 1L당 요금
    # [B사] q : r리터 이하 요금, s : (r리터 초과 시) 1L당 요금
    # w : 종민이의 집에서 한 달간 사용하는 수도의 양
    p, q, r, s, w = map(int, input().split())

    aFee = p * w # aFee : A사를 사용할 때의 요금
    # bFee : B사를 사용할 때의 요금
    if w <= r: # (1) w가 r보다 작은 경우
        bFee = q
    else: # (2) w가 r보다 큰 경우
        bFee = q + s * (w - r)
    
    if aFee < bFee:
        print('#', test_case, ' ', aFee, sep = '')
    else:
        print('#', test_case, ' ', bFee, sep = '')