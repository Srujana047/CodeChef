T = int(input())
for i in range(T):
    n=int(input())
    x=n//9
    y=n%9
    ans=x*45+((y*(y+1))//2)
    print(ans)
