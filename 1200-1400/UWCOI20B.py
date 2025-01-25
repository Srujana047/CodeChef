T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    x,y = 0,0
    for i in a:
        if i%2==0:
            x+=1
        else:
            y+=1
    print(x*y)
