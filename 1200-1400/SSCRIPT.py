T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    s = input()
    count = 0
    maxi = 0
    for i in range(len(s)):
        if(s[i] == '*'):
            count +=1 
            maxi = max(count,maxi)
        else:
            count = 0
    if(maxi>=k):
        print("YES")
    else: 
        print("NO")
