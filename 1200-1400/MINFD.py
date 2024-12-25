T = int(input())
for _ in range(T):
    n,x=map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    add,count=0,0
    ans = False
    for i in range(n):
        add+=a[i]
        count+=1
        if(add>=x):
            ans = True
            break
    if(ans==True):
        print(count)
    else:
        print(-1)
