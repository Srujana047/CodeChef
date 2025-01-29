T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if len(a)==0 or 1 in a:
        print(-1)
    elif len(a)==1:
        print(2)
    else:
        print(sum(a)-a[-1]+2)
