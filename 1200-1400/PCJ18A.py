T = int(input())
for _ in range(T):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = False
    for i in a:
        if i >= x:
           ans = True
           break
    if(ans==True):
        print("YES")
    else:
        print("NO")
