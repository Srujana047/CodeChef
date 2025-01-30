T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans=sum(a)
    print(ans,end=' ')
    for i in range(n-1):
        ans-=a[i]
        print(ans,end=' ')
    print()
