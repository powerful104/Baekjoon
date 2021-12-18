import collections as co
nums = int(input())
for _ in range(nums):
    num=int(input())
    li=[]
    n = 1
    while True:
        n+=1
        if num==1:
            break
        if num%n==0:
            li.append(n)
            num=num//n
            n=1
    d=co.Counter(li)
    for i in d.keys():
        print(str(i)+" "+str(d[i]))