num = 0
max_ = 0

for _ in range(4):
    a, b = map(int,input().split())
    num -= a
    num += b
    
    max_ = max(max_, num)

print(max_)