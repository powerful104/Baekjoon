while True:
    num = int(input())
    if num==0:
        break
    li = set(range(2,2*num+1))
    
    for i in range(2,2*num+1):
        if i in li:
            li -= set(range(2*i,2*num+1,i))
    li-=set(range(num+1))
    print(len(li))
