from itertools import permutations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

for i in permutations(numbers, M):
    print(' '.join(map(str,list(i))))