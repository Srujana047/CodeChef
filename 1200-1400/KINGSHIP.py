T = int(input())
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    lm=min(l)
    add=sum(l)
    total=lm*(add-lm)
    print(total)
