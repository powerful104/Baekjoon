a,b= map(int, input().split())
li = list(map(int, input().split()))
lit=[]
lit.append(sum(li[0:0+b]))

for i in range(0, a-b):
    lit.append(lit[i]-li[i]+li[i+b])
    
print(max(lit))