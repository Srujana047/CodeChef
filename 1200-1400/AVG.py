T = int(input())
for _ in range(T):
    n,k,v = map(int,input().split())
    a = list(map(int,input().split()))
    b = (n+k)*v - int(sum(a))
    if b>0 and b%k==0:
        print(b//k)
    else:
        print(-1)
