num = int(input())
li=[]
for _ in range(num):
    li.append(float(input()))
result = li[0]
cur = 1
for i in range(0, num):
    cur *= li[i]
    result = max(result, cur)
    if cur <= 1:
        cur = 1

print("%.3f" %result)