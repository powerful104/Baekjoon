x1,y1= map(int, input().split())
x2,y2= map(int, input().split())
x3,y3= map(int, input().split())
tmp = x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1 #행렬식이용한 삼각형의 넓이 구하기
if tmp > 0:
    print(1)
elif tmp<0:
    print(-1)
else:
    print(0)