li = list(map(int, list(input())))
if sum(li)%3!=0 or not 0 in li:
    print(-1)
else:
    li.sort(reverse=True)
    print("".join(list(map(str,li))))