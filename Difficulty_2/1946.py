# 1946. 간단한 압축 풀기
# 2022-10-23 (일)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 압축된 문서의 알파벳과 숫자 쌍의 개수
    nWord = [] # nWord : 입력된 문서의 알파벳을 저장한 리스트

    for _ in range(n):
        # alphabet : 압축된 문서의 알파벳, alphabet_count : 압축된 문서의 숫자 쌍의 개수
        alphabet, alphabet_count = input().split()

        for _ in range(int(alphabet_count)):
            nWord.append(alphabet)
    
    print('#', test_case, sep='')
    for i in range(len(nWord)):
        if (i + 1) % 10 == 0:
            print(nWord[i])
        else:
            print(nWord[i], end='')
    
    if (i + 1) % 10 != 0:
        print()
