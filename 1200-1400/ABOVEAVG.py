for _ in range(int(input())):
    n,m,x = map(int,input().split())
    total=n*x 
    if m==x:
        print(0)
    else:
        print(total//(x+1))
