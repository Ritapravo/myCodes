t=int(input())
for i in range(t):
    n=str(input())
    m=int(n[0])
    pos=0
    m1=int(n[0])
    pos2=0
    ma=int(n[0])
    pos1=0
    for j in range (1,len(n)):
        if(int(n[j])<=m):
            m=int(n[j])
            pos=j
        if(int(n[j])>ma):
            ma=int(n[j])
            pos1=j
        if(int(n[j])< m1):
            m1=int(n[j])
            pos2=j
    if(pos==0):
        print(int(n[0:pos1]+n[(pos1+1):]))

    else:
        #print(pos2,pos)
        pos1=0
        ma=int(n[0])
        for j in range(1,pos):
            if(int(n[j])>ma):
                ma=int(n[j])
                pos1=j
        pos3=0
        ma=int(n[0])
        for j in range(1,pos2):
            if(int(n[j])>ma):
                ma=int(n[j])
                pos3=j
        print(min(int(n[0:pos1]+n[(pos1+1):]),int(n[0:pos3]+n[(pos3+1):])))
    
               
