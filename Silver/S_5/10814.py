import sys
num = int(input())
li=[]
for i in range(num):
    li.append(list(sys.stdin.readline().split()))
li = sorted(li, key=lambda x : int(x[0]))
for i in li:
    for k in range(2):
        print(i[k],end=" ")
    print()