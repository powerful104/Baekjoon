import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int, input().split()))

left= 0
right = max(trees)

answer = 0

while(True):
    middle = (left + right) // 2
    taking = 0
    
    for i in trees:
        taking += max(0, i - middle)
        if taking >= M:
            break
    
    if taking >= M:
        left = middle + 1
        answer = middle
    else:
        right = middle - 1
    
    if left > right:
        break

print(answer)