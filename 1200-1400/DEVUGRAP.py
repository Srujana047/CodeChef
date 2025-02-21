T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    ans = 0
    for i in s:
        x=i%k
        if x==min(x,k-x) and (i-x)!=0:
            ans+=x
        else:
            ans+=k-x
    print(ans)
