def three(rec_num, num, sum_):
    if rec_num == 1:
        if (sum_ + num) % 3 == 0:
            return 1
        return 0
    else:
        ans = 0
        for i in range(3):
            ans += three(rec_num-1, i, sum_+i)
        return ans

N = int(input())

print(three(N,1,1) + three(N,2,2))