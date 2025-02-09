T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        a[0] |= a[i]
    ans = 0
    while a[0] > 0:
        if a[0] & 1:
            ans += 1
        a[0] = a[0] >> 1
    print(ans)
