import sys
def P(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    elif num==3:
        return 4
    else:
        return P(num-3)+P(num-2)+P(num-1)
num = int(input())

for _ in range(num):
    print(P(int(sys.stdin.readline())))