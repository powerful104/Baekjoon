lists = []
for _ in range(5):
    lists.append(int(input()))
print(min(lists[:3]) + min(lists[3:]) - 50)