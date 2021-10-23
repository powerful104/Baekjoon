import sys
num = int(input())
li=[]
for i in range(num):
    li.append(list(map(int,sys.stdin.readline().split())))
li = sorted(li, key=lambda x : (x[0], x[1]))
for i in li:
    for k in range(2):
        print(i[k],end=" ")
    print()