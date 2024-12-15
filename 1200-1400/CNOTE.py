T = int(input())
for i in range(T):
    x,y,k,n = map(int,input().split())
    ans = 0
    for i in range(n):
        p,c = map(int,input().split())
        if k>=c and x<=y+p:
            ans=1
    if(ans==1):
        print("LuckyChef")
    else:
        print("UnluckyChef")
