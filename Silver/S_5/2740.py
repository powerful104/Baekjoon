def dot(arr1, arr2):
    answer = [ len(arr2[0])*[0] for i in range (len(arr1)) ]
    for i in range (len(answer) ):
        for j in range ( len(answer[i]) ):
            for k in range ( len(arr1[i] ) ):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

a=[]
b=[]

N, M = map(int,input().split())
for _ in range(N):
    a.append(list(map(int,input().split())))
M, k = map(int,input().split())
for _ in range(M):
    b.append(list(map(int,input().split())))

c = dot(a, b)

for i in c:
    print(' '.join(map(str, i)))