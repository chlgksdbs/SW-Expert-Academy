# 1974. 스도쿠 검증
# 2022-11-15 (화)

T = int(input())

for test_case in range(1, T + 1):
    answer = 1 # answer : 정답
    sudoku = [] # sudoku : 9 x 9 크기의 퍼즐 데이터

    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    
    # num_dic : 1부터 9까지의 숫자를 count 하는 딕셔너리 자료형
    num_dic = {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0
    }

    for i in range(9):
        # (1) 가로 부분 검사
        for j in range(9):
            num_dic[str(sudoku[i][j])] += 1
        if max(num_dic.values()) != min(num_dic.values()):
            answer = 0
            break
        
        # (2) 세로 부분 검사
        for j in range(9):
            num_dic[str(sudoku[j][i])] += 1
        if max(num_dic.values()) != min(num_dic.values()):
            answer = 0
            break
    
    # (3) 3 x 3 크기의 작은 격자 검사
    for i in range(0, 9, 3):
        for j in range(0, 3):
            for k in range(3):
                num_dic[str(sudoku[j][i + k])] += 1
        if max(num_dic.values()) != min(num_dic.values()):
            answer = 0
            break
        
        for j in range(3, 6):
            for k in range(3):
                num_dic[str(sudoku[j][i + k])] += 1
        if max(num_dic.values()) != min(num_dic.values()):
            answer = 0
            break
        
        for j in range(6, 9):
            for k in range(3):
                num_dic[str(sudoku[j][i + k])] += 1
        if max(num_dic.values()) != min(num_dic.values()):
            answer = 0
            break

    print('#', test_case, ' ', answer, sep = '')
