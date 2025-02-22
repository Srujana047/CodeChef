T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    x = [0]*n
    f = 1
    for i in a:
        x[i-1] +=1
        if(max(x)-min(x) > 1): 
            f = 0
            break
    if f: 
        print("YES")
    else: 
        print("NO")
