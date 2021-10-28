num = int(input())
fn = 0
fn1 = 1
ans = fn1
li=[]
check=0
for _ in range(num):
    ans=fn+fn1
    fn=fn1
    fn1=ans%15746
    ans%=15746
print(ans%15746)