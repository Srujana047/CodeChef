tw,tr,c1,c2=0,0,0,0
T = int(input())
for i in range(T):
    r,w=map(int,input().split())
    if (r<tr) or (tw>w) or (c2==1):
        c1=1
    else:
        pass
    if (w==10):
        c2=1
    tr=max(r,tr)
    tw=max(w,tw)
if c1==0:
    print("YES")
else:
    print("NO")
