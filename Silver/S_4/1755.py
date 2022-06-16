
number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def num2string(num):
    if num >= 10:
        return number[num//10] + ' ' + number[num%10]
    else:
        return number[num]


N, M = map(int, input().split())

li = [[num2string(i), i] for i in range(N, M+1)]
li.sort()
flag = 0
for i in range(len(li)):
    if i != 0 and i%10 == 0:
        print()
    print(li[i][1], end = ' ')