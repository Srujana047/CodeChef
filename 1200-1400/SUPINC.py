T = int(input())
for i in range(T):
    n,k,x = map(int,input().split())
    a = 2**(k-1)
    if(a<=x):
        print("YES")
    else: 
        print("NO")
