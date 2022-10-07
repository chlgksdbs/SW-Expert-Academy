# 2056. 연월일 달력
# 2022-10-07 (금)

T = int(input())

for test_case in range(1, T + 1):
    dayList = input() # dayList : 연월일을 문자열로 입력

    year = dayList[0:4] # year : 년
    month = dayList[4:6] # month : 월
    day = dayList[6:8] # day : 일

    if int(month) < 1 or int(month) > 12: # 월 형식이 맞지 않은 경우, -1을 출력하고 아래 명령어를 건너뛴다.
        print('#', test_case, ' ', -1, sep='')
        continue
    
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12: # 1 ~ 31일까지 있는 월
        if int(day) < 1 or int(day) > 31:
            print('#', test_case, ' ', -1, sep='')
            continue
        else:
            print('#', test_case, ' ', year, '/', month, '/', day, sep='')
    elif int(month) == 2: # 1 ~ 28일까지 있는 월
        if int(day) < 1 or int(day) > 28:
            print('#', test_case, ' ', -1, sep='')
            continue
        else:
            print('#', test_case, ' ', year, '/', month, '/', day, sep='')
    else: # 1 ~ 30일까지 있는 월
        if int(day) < 1 or int(day) > 30:
            print('#', test_case, ' ', -1, sep='')
            continue
        else:
            print('#', test_case, ' ', year, '/', month, '/', day, sep='')