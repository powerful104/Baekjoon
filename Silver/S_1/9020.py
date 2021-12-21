import sys
a=0
b=10000
li = set(range(2,b+1))

for i in range(2, b+1):
    if i in li:
        li -= set(range(2*i,b+1,i))
li-=set(range(a))
li=list(li)
li.sort()

io=0
jo=0
num=int(input())
for _ in range(num):
    n=int(sys.stdin.readline())
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]+li[j]>n:
                break
            elif li[i]+li[j]==n:
                io=i
                jo=j
    print(min(li[io],li[jo]),max(li[io],li[jo]))