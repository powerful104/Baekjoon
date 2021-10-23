for _ in range(int(input())):
    maxs=""
    maxl=0
    for _ in range(int(input())):
        a,b= map(str, input().split())
        if int(b)>maxl:
            maxs=a
            maxl=int(b)
    print(maxs)