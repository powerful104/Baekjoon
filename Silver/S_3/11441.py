import sys
input = sys.stdin.readline

numa = int(input())
li = list(map(int, input().split()))
sumli=[]
su = 0
for i in range(numa):
    su += li[i]
    sumli.append(su)
numb = int(input())
for _ in range(numb):
    a, b = map(int, input().split())
    if a>1:
        print(sumli[b-1]-sumli[a-2])
    else:
        print(sumli[b-1])