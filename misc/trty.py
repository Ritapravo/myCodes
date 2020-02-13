from collections import defaultdict
t=int(input())
for _ in range(t):
    n= int(input())
    l=[]
    for i in range(n):
        (s,b)=map(str,input().split())
        l.append((s,b))
    d=defaultdict(list)
    for i in range(n):
        if (l[i][0] not in d):
            d[l[i][0]].append(0)
            d[l[i][0]].append(0)
        
    for i in range(n):
        x= l[i][0]
        y= l[i][1]
        if (y =="0"):
            d[x][0]+=1
        else:
            d[x][1]+=1
    s=0
    for i in d:
        s+=max(d[i])
    print(s)
        
