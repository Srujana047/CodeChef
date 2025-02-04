T = int(input())
for _ in range(T):
    l = int(input())
    s = input()
    c = 0
    ans = False
    for i in range(l):
        c += int(s[i])
        if(c>=((i+1)/2)):
            print("YES")
            ans = True
            break
    if ans == False:
        print("NO")
