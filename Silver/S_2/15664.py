from itertools import combinations

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

for i in sorted(list(set(map(tuple, combinations(numbers, M))))):
    print(' '.join(map(str, i)))