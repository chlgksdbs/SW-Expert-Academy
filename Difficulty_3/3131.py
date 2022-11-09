# 3131. 100만 이하의 모든 소수
# 2022-11-09 (수)

'''
모든 약수에 대하여, 가운데 약수를 기준으로 해서 각 등식이 대칭적인 형태를 보인다.
따라서 특정한 자연수 X가 소수인지 확인하기 위하여 바로 가운데 약수까지만 '나누어떨어지는지' 확인하면 된다.
다시 말해 제곱근까지만 (가운데 약수까지만) 확인하면 된다는 점을 기억하자.
'''

import math

# n이 소수인지 판별하는 함수
def getPrimeNumber(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        # n이 해당 수로 나누어 떨어지는 경우
        if n % i == 0:
            return False
    
    return True

for i in range(2, 1000001):
    if getPrimeNumber(i):
        print(i, end = ' ')
