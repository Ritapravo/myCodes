
#Kadene's algorithm for maximum sub-array sum

def max_subarray_sum(arr,size):
    m=0 #stores max
    c=0 #stores current max
    for i in range(size):
        c=max(arr[i],c+arr[i])
        m=max(c,m)
        print(c)
    return m



#Sieve of Eratosthenes for finding prime numbers in a range

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


#Lowest Commmon Subsequence using Dynamic Programmimg

def LCS(s1,s2):
    n1=len(s1)
    n2=len(s2)
    arr=[[0 for i in range(n1+1)] for j in range(n2+1)]
    for i in range(1,n2+1):
        
        for j in range(1,n1+1):
            if(s2[i-1]==s1[j-1]):
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
            
    """for k in arr:
        print(k)"""
    lcs=""
    for i in range(n1,0,-1):
        if(arr[n2][i]==arr[n2][i-1]+1):
            lcs=lcs+s1[i-1]
    return(lcs[::-1])
    #return arr[n2][n1]
        
