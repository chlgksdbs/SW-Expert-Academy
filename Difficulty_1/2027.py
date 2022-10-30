# 2027. 대각선 출력하기
# 2022-10-30 (일)

for i in range(5):
    for j in range(5):
        if j == i:
            print('#', end = '')
        else:
            print('+', end = '')
    print()