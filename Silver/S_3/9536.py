T = int(input())

for _ in range(T):
    say = input().split()
    animals = []

    while True:
        s = input().split()
        if s[0] == "what":
            break
        animals.append(s[-1])

    for i in say:
        if i not in animals:
            print(i, end=" ")
    print()