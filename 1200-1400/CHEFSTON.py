T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = []
    for i in range(n):
        y = k//a[i]
        z = y*b[i]
        x.append(z)
    print(max(x))
