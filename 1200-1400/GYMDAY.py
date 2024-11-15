T = int(input())
for i in range(T):
    d,x,y = map(int,input().split())
    c=0
    n = -1
    if y>=x:
        print(0)
    else:
        while(y!=0):
            y-=1
            c+=1
            z = (d*c*x)/100
            b = x-z
            if(b<=y):
                n=c
                break
        print(n)
