import sys
input = sys.stdin.readline
n = int(input())
cnt = [0 for i in range(10000+1)]#10000까지의 숫자를 각 숫자의 개수를 세기위한 배열 지정

for i in range(n):
    cnt[int(input())] += 1 #배열의 인덱스 이용한 접근으로 빠른 정렬 가능
for i in range(1, 10000+1): # 정렬된 요소를 출력
    for j in range(cnt[i]):
        print(i)
