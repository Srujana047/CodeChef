T=int(input())
while T:
    a=input()
    s={'c','h','e','f'}
    count=0
    for i in range(len(a)-3):
        if set(a[i:i+4])==s:
            count=count+1 
    if count!=0:
        print(f'lovely {count}')
    else:
        print('normal')
    T=T-1    
        
