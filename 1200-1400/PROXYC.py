T = int(input())
for _ in range(T):
    n=int(input())
    a=input()
    b=list(a)
    p=a.count('P')
    if p/n>=0.75:
        print('0')
    else:
        c=p
        for i in range(2,n-2):
            if b[i]=='A' and (b[i-1]=='P' or b[i-2]=='P') and (b[i+1]=='P' or b[i+2]=='P'):
                p+=1
                if p/n>=0.75:
                    print(p-c)
                    break
        else:
            print(-1)
