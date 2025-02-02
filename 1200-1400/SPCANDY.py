T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    if(k==0):
        print(0,n)
    else: 
        print(n//k,n-((n//k)*k))
