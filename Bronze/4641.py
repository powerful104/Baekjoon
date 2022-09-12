while(True):
    nums = list(map(int,input().split()))
    
    if nums[0] == -1:
        break
    
    ans = -1
    
    for num in nums:
        if num*2 in nums:
            ans += 1
    
    print(ans)