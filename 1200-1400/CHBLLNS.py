T = int(input())
for i in range(T):
    r,g,b = map(int,input().split())
    k = int(input())
    x=0
    if(r>=k):
        x+=k-1
    if(g>=k):
        x+=k-1
    if(b>=k):
        x+=k-1
    if(r<k):
        x+=r  
    if(g<k):
        x+=g 
    if(b<k):
        x+=b
    print(x+1)
