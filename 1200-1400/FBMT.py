from collections import defaultdict
T=int(input())
for i in range(T):
    n=int(input())
    d=defaultdict(int)
    for i in range(n):
        d[input()]+=1 
    a=list(d.values())
    b=list(d.keys())
    if len(a)==0:
        print("Draw")
    elif len(a)==1:
        print(b[0])
        continue
    elif a[0]>a[1]:
        print(b[0])
    elif a[0]<a[1]:
        print(b[1])
    else:
        print("Draw")
