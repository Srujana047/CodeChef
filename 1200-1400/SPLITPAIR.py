T = int(input())
for _ in range(T):
    n=input()
    x=int(n[-1])%2
    for i in range(len(n)-2,-1,-1):
        if int(n[i])%2==x:
            print("YES")
            break
    else:
        print("NO")
