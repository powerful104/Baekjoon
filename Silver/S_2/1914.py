num = int(input())
answer = []

def hanoi(n, start, via, to):
    if n == 1:
        answer.append([start, to])
    else:
        hanoi(n-1, start, to, via)
        answer.append([start, to])
        hanoi(n-1, via, start, to)
    return

if num > 20:
    print(2**num-1)
else:
    hanoi(num,1,2,3)
    print(len(answer))
    for i in answer:
        print(i[0],i[1])