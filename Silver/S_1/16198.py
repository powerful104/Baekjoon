N = int(input())
numbers = list(map(int,input().split()))
answer = 0

while N > 2:
    print(numbers)
    tmp_max = 0
    tmp_ind = numbers.index(max(numbers))
    for i in range(1, N - 1):
        if numbers[i-1] * numbers[i+1] > tmp_max:
            tmp_max = numbers[i-1] * numbers[i+1]
            tmp_ind = i
        elif numbers[i-1] * numbers[i+1] == tmp_max and numbers[i] < numbers[tmp_ind]:
            tmp_ind = i
    answer += tmp_max
    del numbers[tmp_ind]
    N -= 1

print(answer)