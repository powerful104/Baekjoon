N = int(input())
numbers = list(map(int, input().split()))

answer = [0]*N
index = 0

for i in range(1, 1001):
    for j in range(len(numbers)):
        if numbers[j] == i:
            answer[j] = index
            index += 1

print(' '.join(map(str, answer)))