T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = 1
    ans = False
    for i in a:
        c*=i
        if(c%k==0):
            ans = True
            break
    if(ans == True):
        print("YES")
    else:
        print("NO")
