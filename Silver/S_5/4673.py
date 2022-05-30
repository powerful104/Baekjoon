import sys
input = sys.stdin.readline

def self_number(num):
    return num + sum(map(int,list(str(num))))

answer = [0] * 10001

for i in range(1, 10001):
    num = self_number(i)
    if num <= 10000:
        answer[num] = 1
        
for i in range(1, 10001):
    if answer[i] == 0:
        print(i)