num = int(input())
li=[]

for _ in range(num):
    n = int(input())
    if n==0:
        del li[len(li)-1]
    else:
        li.append(n)
print(sum(li))