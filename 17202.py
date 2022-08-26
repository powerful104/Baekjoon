A = list(map(int, list(input())))
B = list(map(int, list(input())))

C = []

for i in range(8):
    C.append(A[i])
    C.append(B[i])

while True:
    tmp = []
    
    for i in range(len(C)-1):
        tmp.append((C[i]+C[i+1])%10)
    
    C = tmp
    
    if len(C) == 2:
        break

print(''.join(map(str,C)))