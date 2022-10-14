# 2007. 패턴 마디의 길이
# 2022-10-14 (금)

T = int(input())

for test_case in range(1, T + 1):
    s = input() # s : 문자열
    sWord = "" # sWord : 패턴 문자열

    for i in range(len(s)):
        if len(sWord) == 0 or sWord[0] != s[i]: # sWord의 첫 문자와 s[i]가 다른 경우
            sWord += s[i]
        else:
            wordCheck = 1 # 패턴 문자열이 일치하는지 확인하는 변수
            idx = i
            for j in range(len(sWord)):
                if i < (len(s) - 1) and sWord[j] == s[idx]: # 문자가 일치하는 경우
                    idx += 1
                else: # 문자가 일치하지 않는 경우
                    wordCheck = 0
                    break
            if wordCheck == 1:
                break
            else:
                sWord += s[i]
    
    print('#', test_case, ' ', len(sWord), sep = '')