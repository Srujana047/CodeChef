for i in range(int(input())):
    a,b,p,q=map(int,input().split())
    x=a+b
    y=p+q
    n=x%2
    m=y%2
    if a==p and b==q:
        print(0)
    elif m==n: 
        print("2")
    else:
        print("1")
