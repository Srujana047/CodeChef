T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    a=[]
    add = 0
    for i in range(n):
        add=0
        for j in range(n):
            if(f[i]==f[j]):
                add+=p[j]
        a.append(add)
    print(min(a))
