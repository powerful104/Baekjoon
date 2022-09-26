N = int(input())
if N < 11:
    print(N-1)
else:
    nums = [[str(i)] for i in range(10)]

    ans = 10
    try:
        for i in range(0, 10):
            new_nums = [[] for _ in range(10)]
            for j in range(i,10):
                for k in range(0,j):
                    for num in nums[k]:
                        new_nums[j].append(str(j)+num)
                        ans += 1
                        if ans == N:
                            print(str(j)+num)
                            raise NotImplementedError
            nums = list(new_nums)
        else:
            print(-1)
    except:
        print("",end = "")