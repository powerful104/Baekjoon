a,b= map(int, input().split())
li = [[0 for col in range(a) ] for row in range(b)]

for i in range(a):
    li[0][i]=1
    
for j in range(b):
    li[j][0]=1
    
for i in range(1,b):
    for j in range(1,a):
        li[i][j]=(li[i-1][j]+li[i][j-1]+li[i-1][j-1])%1000000007
        
print(li[b-1][a-1])