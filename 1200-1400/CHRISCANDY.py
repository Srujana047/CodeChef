t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    maxi = a[0]
    for i in range(1,len(a)):
        if a[i]>maxi:
            maxi = a[i]
        else:
            b+=1
    print(b)
