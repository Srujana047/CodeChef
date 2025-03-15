T = int(input())
for i in range(T):
    a1,a2,a3,c1,c2,c3 = map(int,input().split())
    l = sorted([(a1,c1),(a2,c2),(a3,c3)])
    if (l[0][0] == l[1][0] and l[0][1] != l[1][1]) or \
   (l[1][0] == l[2][0] and l[1][1] != l[2][1]) or \
   (l[0][0] < l[1][0] and l[0][1] >= l[1][1]) or \
   (l[1][0] < l[2][0] and l[1][1] >= l[2][1]):
        print("NOT FAIR")
    else:
        print("FAIR")
