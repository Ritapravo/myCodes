def max_subarray_sum(arr,size):
    m=0 #stores max
    c=0 #stores current max
    for i in range(size):
        c=max(arr[i],c+arr[i])
        m=max(c,m)
        print(c)
    return m


def sieve(n):
    primes=[True]*(n+1)
    p=2
    while(p*p<=n):
        if(primes[p]==True):
            for i in range(2*p,n+1,p):
                primes[i]=False
        p+=1
    primes[0]=False
    primes[1]=False
    for i in range(n+1):
        if (primes[i]==True):
            print (i)
