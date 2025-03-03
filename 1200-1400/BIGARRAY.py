T = int(input())
for i in range(T):
    n,s = map(int,input().split())
    t = (n*(n+1))//2
    x=t-s
    if x>=1 and x<=n:
        print(x)
    else:
        print(-1)
