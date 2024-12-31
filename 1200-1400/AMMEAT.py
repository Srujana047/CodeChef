t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort(reverse = True)
    add = 0
    count = 0
    for i in range(len(p)):
        add+=p[i]
        count+=1
        if(add>=m):
            break
    if add < m:
        print(-1)
    else:
        print(count)
