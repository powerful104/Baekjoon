N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(M):
    numbers.sort()
    tmp_sum = numbers[0] + numbers[1]
    numbers[0] = tmp_sum
    numbers[1] = tmp_sum

print(sum(numbers))