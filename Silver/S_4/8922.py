tc=int(input())

for _ in range(tc):
    li=[]
    n=int(input())
    li.append(tuple(map(int, input().split())))
    
    while True:
        tl=[]
        t=0
        
        for i in range(len(li[-1])):
            if i==0:
                t=abs(li[-1][i-1]-li[-1][i])
            else:
                tl.append(abs(li[-1][i-1]-li[-1][i]))
                
        tl.append(t)
        
        if sum(tl)==0:
            print("ZERO")
            break
        elif tuple(tl) in li:
            print("LOOP")
            break
        else:
            li.append(tuple(tl))