for _ in range(int(input())):
    s=list(map(int,input().split()))
    a=[]
    for i in range(16):
        c=0
        for j in range(16):
            if i!=j and s[i]>s[j]:
                c+=1
        a.append(c)
    n=len(a)
    for i in range(n):
        if a[i]<=14 and a[i]>=7:
            print(3, end=' ')
        elif a[i]<=6 and a[i]>=3:
            print(2,end=' ')
        elif a[i]>=1 and a[i]<=2:
            print(1,end=' ')
        elif a[i]==15:
            print(4,end=' ')
        else:
            print(0,end=' ')
