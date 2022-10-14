# 1989. 초심자의 회문 검사
# 2022-10-14 (금)

T = int(input())

for test_case in range(1, T + 1):
    s = input() # s : 문자열
    answer = 0 # answer : 회문인지 아닌지 판별하는 변수

    idx_start = 0 # idx_start : 시작 부분의 인덱스
    idx_end = len(s) - 1 # idx_end : 끝 부분의 인덱스

    while True:
        if idx_start == idx_end: # 두 변수가 중간 부분에서 만나는 경우
            answer = 1
            break
        
        if s[idx_start] == s[idx_end]:
            idx_start += 1
            idx_end -= 1
        else:
            break
    
    print('#', test_case, ' ', answer, sep = '')