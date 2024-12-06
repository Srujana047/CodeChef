T = int(input())
for i in range(T):
    a,b,c,d = map(int,input().split())
    if (a==0) or (b==0) or (c==0) or (d==0) :
        print("Yes")
    elif (a+b==0) or (a+c==0) or (a+d==0) or (c+b==0) or (d+b==0) or (c+d==0):
        print("Yes")
    elif (a+b+c == 0) or (b+c+d == 0) or (c+d+a == 0) or (d+a+b == 0):
        print("Yes")
    elif (a+b+c+d == 0):
        print("Yes")
    else :
        print("No")
