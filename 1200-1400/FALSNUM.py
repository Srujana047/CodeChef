T = int(input())
for i in range(T):
    a = list(input())
    if(a[0]=='1'):
        print("10",end="")
        for i in range(1,len(a)):
            print(a[i],end="")
    else:
        print("1",end="")
        for i in range(0,len(a)):
            print(a[i],end="")
    print()
