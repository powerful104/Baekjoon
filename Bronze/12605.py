N = int(input())

for i in range(N):
    words = reversed(list(input().split()))
    print("Case #" + str(i+1) + ": " + " ".join(words))