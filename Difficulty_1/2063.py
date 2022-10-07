# 2063. 중간값 찾기
# 2022-10-07 (금)

n = int(input()) # n : 수의 개수(항상 홀수)
nList = list(map(int, input().split())) # nList : n개의 점수를 담는 리스트

nList.sort() # 오름차순 정렬

print(nList[n // 2]) # 중간값 출력