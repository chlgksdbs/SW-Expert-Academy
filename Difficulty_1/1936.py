# 1936. 1대1 가위바위보
# 2022-10-11 (화)

# a와 b가 낸 손 (1 : 가위, 2 : 바위, 3 : 보)
a, b = map(int, input().split())

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
else:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')