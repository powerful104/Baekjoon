import sys
num=int(input())
li={}

for _ in range(num):
    a, b = map(str, sys.stdin.readline().split())
    if b=="enter":
        li[a]=True
    else:
        li[a]=False
        
d=sorted(li.keys(),reverse=True)

for i in d:
    if li[i]==True:
        print(i)
