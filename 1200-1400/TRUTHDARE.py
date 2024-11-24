T = int(input())
for i in range(T):
    tr = int(input())
    r = set(map(int,input().split())) #truth of ram
    dr = int(input())
    d = set(map(int,input().split())) #dare of ram
    ts = int(input())
    s = set(map(int,input().split())) #truth of shyam
    ds = int(input())
    a = set(map(int,input().split())) #dare of shyam
    one = s.issubset(r)
    two = a.issubset(d)
    if one == True and two==True:
        print('yes')
    else:
        print('no')
