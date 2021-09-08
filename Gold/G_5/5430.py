num = int(input())
for _ in range(num):
    p = list(input().strip())
    n = int(input())
    arr = list(map(int,input().replace("["," ").replace("]"," ").replace(","," ").split()))
    check=0
    r=1
    for i in p:
        if i=="R":
            r*=-1
        else:
            if len(arr)==0:
                print("error")
                check=1
                break
            else:
                if r<0:
                    del arr[len(arr)-1]
                else:
                    del arr[0]
    if check!=1:
        if r < 0:
            arr.reverse()
        print("[", end="")
        print(",".join(map(str,arr)), end="")
        print("]")