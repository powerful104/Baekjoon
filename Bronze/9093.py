N = int(input())

for _ in range(N):
    s = input().split()
    for w in s:
        print(''.join(reversed(list(w))),end = " ")
    print()