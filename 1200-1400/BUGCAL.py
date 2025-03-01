T = int(input())
for i in range(T):
    a,b=map(int,input().split())
    x,y=0,1
    while a>0 or b>0:
        m=a%10
        n=b%10
        t=(m+n)%10
        x+=t*y
        y*=10
        a//=10
        b//=10
    print(x)
