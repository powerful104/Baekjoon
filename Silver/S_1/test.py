import sys
input = sys.stdin.readline

def main() :
    num = int(input())
    arr = set(list(map(int ,input().split())))
		
    if len(arr) < num:
        print("NO")
    else:
        print("YES")

main()