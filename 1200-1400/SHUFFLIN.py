T = int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    x=n//2 
    e=0
    o=0
    c=0
    while c<n:
        if a[c]%2==0:
            e+=1 
        else:
            o+=1 
        c+=1 
    if n%2==0:
        print(min(x,o)+min(x,e))
    else:
        print(min(x,o)+min(x+1,e))
