from itertools import permutations

n = int(input())
nums = list(map(int,input().split()))
tmp = list(map(int,input().split()))
exs = [0]*tmp[0] + [1]*tmp[1] + [2]*tmp[2] + [3]*tmp[3]

mx = -1000000001
mn = 1000000001
exs = list(set(list(permutations(exs,len(exs)))))

for i in exs:
    tmpn = nums[0]
    for j in range(len(i)):
        if i[j] == 0:
            tmpn += nums[j+1]
        elif i[j] == 1:
            tmpn -= nums[j+1]
        elif i[j] == 2:
            tmpn *= nums[j+1]
        else:
            if (tmpn > 0 and nums[j+1] > 0) or (tmpn < 0 and nums[j+1] < 0):
                tmpn //= nums[j+1]
            else:
                tmpn = -1*(abs(tmpn)//abs(nums[j+1]))
    if tmpn > mx:
        mx = tmpn
    if tmpn < mn:
        mn = tmpn
print(mx)
print(mn)

"""
숫자와 연산자로 나누어 연산자는 permutation을 통해 순열을 구하고 해당 순열에서 중복되는것을 제거하기위해 set을 사용,
해당 순열을 하나씩 참고하며 계산을 실제로 진행해보고 max와 min을 찾았다.
"""
