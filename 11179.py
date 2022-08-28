N = int(input())
bN = list(bin(N)[2:])
print(int(''.join(bN[::-1]), 2))