def P(num):
    li=[1]*(num+1)
    li[1]=0
    for i in range(4,num+1):
        lit=[]
        if i%3==0:
            lit.append(li[i//3])
        if i%2==0:
            lit.append(li[i//2])
        lit.append(li[i-1])
        li[i]=min(lit)+1
    return li[num]

n = int(input())

print(P(n))