import sys
num = int(input())
Deque=[]
for _ in range(num):
    li = list(map(str, sys.stdin.readline().split()))
    n=0
    if li[0]=="push_front":
        Deque = [int(li[1])]+Deque
    elif li[0]=="push_back":
        Deque.append(int(li[1]))
    elif li[0] == "pop_front":
        if len(Deque)!=0:
            print(Deque.pop(0))
        else:
            print("-1")
    elif li[0] == "pop_back":
        if len(Deque)!=0:
            print(Deque.pop(-1))
        else:
            print("-1")
    elif li[0] == "size":
        print(len(Deque))
    elif li[0] == "empty":
        print(int(len(Deque)==0))
    elif li[0] == "front":
        if len(Deque)!=0:
            print(Deque[0])
        else:
            print("-1")
    else:
        if len(Deque)!=0:
            print(Deque[-1])
        else:
            print("-1")