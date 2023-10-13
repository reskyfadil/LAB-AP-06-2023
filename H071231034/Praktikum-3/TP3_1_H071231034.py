n=int(input())
x,y=0,1
for _ in range(n):
    print(x, end=" ")
    z = x+y
    x = y
    y = z