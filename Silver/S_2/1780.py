cntm1 = 0
cnt0 = 0
cnt1 = 0

def calc(size, arr):
    global cntm1
    global cnt0
    global cnt1
    if size == 1 :
        if arr[0][0] == 0:
            cnt0 += 1
        elif arr[0][0] == 1:
            cnt1 += 1
        elif arr[0][0] == -1:
            cntm1 += 1
        return
    check = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == arr[0][0]:
                check += 1
    if check != size**2:
        calc(size//3, [arr[i][:size//3] for i in range(size//3)])
        calc(size//3, [arr[i][size//3:size//3*2] for i in range(size//3)])
        calc(size//3, [arr[i][size//3*2:] for i in range(size//3)])
        calc(size//3, [arr[i][:size//3] for i in range(size//3,size//3*2)])
        calc(size//3, [arr[i][size//3:size//3*2] for i in range(size//3,size//3*2)])
        calc(size//3, [arr[i][size//3*2:] for i in range(size//3,size//3*2)])
        calc(size//3, [arr[i][:size//3] for i in range(size//3*2,size)])
        calc(size//3, [arr[i][size//3:size//3*2] for i in range(size//3*2,size)])
        calc(size//3, [arr[i][size//3*2:] for i in range(size//3*2,size)])
    elif arr[0][0] == 0:
        cnt0 += 1
    elif arr[0][0] == 1:
        cnt1 += 1
    elif arr[0][0] == -1:
        cntm1 += 1

arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
calc(len(arr),arr)
print(cntm1)
print(cnt0)
print(cnt1)

"""
재귀함수 호출시 배열을 복사하는데에 시간이초과됨으로 고려됨
"""