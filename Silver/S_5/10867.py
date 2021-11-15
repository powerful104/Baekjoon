lia = [0] * 2001
num = int(input())
li = list(map(int, input().split()))
for i in li:
    lia[i+1000]=1
for i in range(len(lia)):
    if lia[i]==1:
        print(i-1000,end="")
        if i != len(lia)-1:
            print(" ",end="")