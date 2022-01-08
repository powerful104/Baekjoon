import sys
num = int(input())
stack=[]

for _ in range(num):
    li = list(map(str, sys.stdin.readline().split()))
    n=0
    if li[0]=="push":
        stack.append(int(li[1]))
    elif li[0] == "pop":
        if len(stack)!=0:
            print(stack.pop(0))
        else:
            print("-1")
    elif li[0] == "size":
        print(len(stack))
    elif li[0] == "empty":
        print(int(len(stack)==0))
    elif li[0] == "front":
        if len(stack)!=0:
            print(stack[0])
        else:
            print("-1")
    else:
        if len(stack)!=0:
            print(stack[-1])
        else:
            print("-1")