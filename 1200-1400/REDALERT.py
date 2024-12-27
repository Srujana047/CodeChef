T = int(input())
for _ in range(T):
    n,d,h = map(int,input().split())
    a = list(map(int,input().split()))
    add=0
    for i in range(n):
        if a[i] > 0:
            add += a[i]
        elif a[i] == 0:
            add -= d
            if add < 0:
                add =0
        if add > h:
            print('YES')
            break
    else:
        print('NO')
