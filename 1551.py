N, K = map(int, input().split())
A = list(map(int,input().split(",")))

for _ in range(K):
    B = []
    for i in range(len(A)-1):
        B.append(A[i+1]-A[i])
    A = list(B)

print(','.join(list(map(str,A))))