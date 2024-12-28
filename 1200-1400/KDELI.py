for i in range(int(input())):
    n,k,l = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    add = 0
    for i in range(l-1,n,k):
        add+=a[i]
    print(add)
