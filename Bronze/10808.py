s = input()

answer = [0] * 26

for c in s:
    answer[ord(c)-97] += 1

print(' '.join(list(map(str, answer))))