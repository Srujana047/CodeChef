T = int(input())
for _ in range(T):
    s = input()
    i = 0
    n = len(s)
    while i<n and s[i] == "C":
        i+=1  
    while i<n and s[i] == "E":
        i+=1 
    while i<n and s[i] == "S":
        i+=1 
    
    if i == len(s):
        print("yes")
    else:
        print("no")
    
