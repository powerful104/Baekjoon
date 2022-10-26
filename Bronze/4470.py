N = int(input())
words = []
for i in range(N):
    words.append(str(i+1) + ". " + input())
print('\n'.join(words))