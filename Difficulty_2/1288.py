# 1288. 새로운 불면증 치료법
# 2022-11-02 (수)

T = int(input())

for test_case in range(1, T + 1):
    n = input()
    numList = [] # numList : n의 배수에서 본 0에서 9까지의 숫자를 담는 리스트
    answerList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = n # result : 몇 번 양을 세어서 0부터 9까지의 숫자를 보게 됐는지에 대한 변수
    i = 2 # i : 곱하는 수

    while True:
        for x in result:
            if not int(x) in numList:
                numList.append(int(x))
        
        numList.sort() # 오름차순 정렬

        if answerList == numList:
            break
        else:
            result = str(int(n) * i)
            i += 1
    
    print('#', test_case, ' ', result, sep = '')