# 1940. 가랏! RC카!
# 2022-11-10 (목)

T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # n : 입력으로 주어진 command의 수
    rcSpeed = 0 # rcSpeed : 현재 rc 카의 속도
    rcMoveLen = 0 # rcMoveLen : rc 카가 이동한 거리

    for _ in range(n):
        cmd = list(map(int, input().split()))
        
        if len(cmd) == 2:
            if cmd[0] == 1: # 명령어 1 : 가속
                rcSpeed += cmd[1]
            
            else: # 명령어 2 : 감속
                rcSpeed -= cmd[1]
                if rcSpeed < 0:
                    rcSpeed = 0
        
        rcMoveLen += rcSpeed
    
    print('#', test_case, ' ', rcMoveLen, sep = '')