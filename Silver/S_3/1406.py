import sys
input = sys.stdin.readline

left=[]
right=[]
left+=list(input().strip())
num = int(input())

for _ in range(num):
    li = list(map(str, input().split()))
    if li[0] == "L":
        if len(left)>0:
            right.append(left[-1])
            del left[-1]
    elif li[0] == "D":
        if len(right)>0:
            left.append(right[-1])
            del right[-1]
    elif li[0] == "B":
        if len(left)>0:
            del left[-1]
    else:
        left.append(li[1])
right.reverse()
print("".join(left)+"".join(right))