T=int(input())
for i in range (T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c=[0]*n
    for j in range (n):
        c[j]=a[j]*b[j]
    c.sort(reverse=True)
    m=0
    while x>0 and m<n:
        x=x-c[m]
        m=m+1
    if x<=0:
        print(m)
    else:
        print(-1)
