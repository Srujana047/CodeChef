# cook your dish here
T = int(input())
for i in range(T):
    ts=int(input())
    if ts%2==1:
        print((ts-1)//2)
    else:
        while(ts%2==0 and ts!=0):
            ts//=2
        if ts==0:
            print(0)
        else:
            print((ts-1)//2)
