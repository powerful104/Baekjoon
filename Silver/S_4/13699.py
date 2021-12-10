num = int(input())
li=[1]

for _ in range(num):
    su=0
    for i in range(len(li)):
        su+=li[i]*li[len(li)-i-1]
    li.append(su)
print(li[-1])