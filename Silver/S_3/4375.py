while True:
    try:
        num = int(input())
        s=0
        
        for _ in range(len(str(num))):
            s=s*10+1
        while True:
            if s%num==0:
                break
            s=s*10+1
        print(len(str(s)))
    except EOFError:
        break