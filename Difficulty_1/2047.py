# 2047. 신문 헤드라인
# 2022-10-19 (수)

s = input()

for x in s:
    if x.islower():
        print(x.upper(), end='')
    else:
        print(x, end='')