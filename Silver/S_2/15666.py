from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

for i in sorted(list(set(map(tuple,combinations_with_replacement(numbers, M))))):
    print(' '.join(map(str, i)))