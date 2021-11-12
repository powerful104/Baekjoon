li = [0] * 20000001
num = int(input())
lia = list(map(int, input().split()))

for i in lia:
    li[i+10000000]=1
    
n = int(input())
lib = list(map(int, input().split()))

for i in range(n):
    print(li[lib[i]+10000000],end="")
    if i!=n:
        print(" ",end="")