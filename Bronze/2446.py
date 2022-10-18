N = int(input())

for i in range(N):
    for j in range(i):
        print(" ",end='')
    for j in range(N-i):
        print("*",end='')
    for j in range(N-1-i):
        print("*",end='')
    print()
for i in range(N-2,-1,-1):
    for j in range(i):
        print(" ",end='')
    for j in range(N-i):
        print("*",end='')
    for j in range(N-1-i):
        print("*",end='')
    print()