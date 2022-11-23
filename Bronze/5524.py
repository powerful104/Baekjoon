N = int(input())
names = []
for _ in range(N):
    names.append(input())

for i in list(map(lambda x: x.lower(), names)):
    print(i)