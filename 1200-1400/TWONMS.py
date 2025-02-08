T=int(input())
for i in range(T):
    a,b,n=map(int,input().split())
    if n&1==0:
        if a>b:
            print(a//b)
        else:
            print(b//a)
    else:
        a*=2 
        if a>b:
            print(a//b)
        else:
            print(b//a)
