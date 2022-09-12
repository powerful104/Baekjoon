N = int(input())

fn1 = 0
fn2 = 1

for _ in range(N-1):
    fn1, fn2 = fn2, fn2+fn1

print(fn2)