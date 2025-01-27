a = '415926530119026040722614947737296840070086399613316'*10**6
T = int(input())
for i in range(T):
    k = int(input())
    if k == 0:
        print('3')
    elif k == 1:
        print('3.1')
    else:
        print('3.1'+ a[:k-1])
