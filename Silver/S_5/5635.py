N = int(input())

names = []

for _ in range(N):
    s = input().split()
    names.append([s[0]] + list(map(int, s[1:])))

names = sorted(names, key = lambda x: (x[3],x[2],x[1]))

print(names[-1][0])
print(names[0][0])