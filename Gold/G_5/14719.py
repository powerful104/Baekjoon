H, W = map(int,input().split())

heights = list(map(int,input().split()))

ans = 0

for i in range(H):
    left = -1
    right = -1
    for j in range(W):
        if heights[j] > i:
            if left == -1:
                left = j
            else:
                right = j
        
        if left != -1 and right != -1:
            ans += right - left - 1
            left = right
            right = -1

print(ans)