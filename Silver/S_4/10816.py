num = int(input())
li = list(map(int, input().split()))
d={}
for i in li:
    d.setdefault(i,0)
    d[i]+=1
n = int(input())
lit = list(map(int, input().split()))
for i in range(n):
    d.setdefault(lit[i],0)
    print(d[lit[i]],end="")
    if i!=n-1:
        print(" ",end="")