T = int(input())
for i in range(T):
    k=int(input())
    if k%2==1:
        print(0)
    else:
        c=1
        x=k//2
        while(x%2==0 and k!=0):
            k-=x
            x=k//2
            c+=1
        print(c)
