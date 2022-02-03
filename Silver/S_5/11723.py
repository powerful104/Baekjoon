import sys
input = sys.stdin.readline

num = int(input())
se=set()

for _ in range(num):
    li = list(map(str, input().split()))
    c = li[0] #command
    if c=="add":
        se.add(int(li[1]))
    elif c=="remove":
        if int(li[1]) in se:
            se.remove(int(li[1]))
    elif c=="check":
        print(int(int(li[1]) in se))
    elif c=="toggle":
        if int(li[1]) in se:
            se.remove(int(li[1]))
        else:
            se.add(int(li[1]))
    elif c=="all":
        se=set(range(1,21))
    else:
        se.clear()
