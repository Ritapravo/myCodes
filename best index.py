def nim(n):
    p=1
    m=p*(p+1)//2
    while(m<=n):
        p+=1
        m=p*(p+1)//2
    return p-1
        
    
N = int(input())
arr = [int(p) for p in str(input()).split()]
#print(arr)
prefix = [0]*(N+1)

for i in range(N):
    prefix[i+1]=prefix[i]+arr[i]

#print(prefix)

index=[0]*(N)
t = nim(N)
m = t*(t+1)//2

for i in range(N):
    if(m+i > N):
        t=t-1
        m = t*(t+1)//2
    
    index[i]=prefix[i+m]-prefix[i]
print(max(index))
        
