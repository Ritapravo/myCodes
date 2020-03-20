import sys
sys.setrecursionlimit(1000000000)

def mi(a, m) : 
      
    g = gcd(a, m) 
      
    if (g != 1) : 
        return -1
          
    else :
        return pow(a, m - 2, m)
        
def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a)

def merge(arr,l,m,r):
    inv = 0
    n1 = m-l+1
    n2 = r-m
    L = []
    R = []
    for i in range(n1):
        L.append(arr[l+i])
    for j in range(n2):
        R.append(arr[m+j+1])
    i = 0
    j = 0
    k = l
    while(i<n1 and j<n2):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inv += m-(l+i)+1
        k += 1
    while(i<n1):
        arr[k] = L[i]
        i = i+1
        k = k+1
    while(j<n2):
        arr[k] = R[j]
        j += 1
        k += 1
    return inv
def ms(arr,l,r):
    inv = 0
    if(l<r):
        m = l + (r-l)//2
        inv += ms(arr,l,m)
        inv += ms(arr,m+1,r)
        inv += merge(arr,l,m,r)
    return inv

def countSubarray(arr, n, k): 
    count = 0
  
    for i in range(0, n): 
        sum = 0
        for j in range(i, n): 
              
            # If sum is less than k 
            # then update sum and  
            # increment count 
            if (sum + arr[j] < k): 
                sum = arr[j] + sum
                count+= 1
            else: 
                break
    return count

for _ in range(int(input())):
    n = int(input())
    s = str(input())
    arr = [0]*(n+1)
    for i in range(n):
        if(s[i] == '('):
            arr[i+1] = 1
        elif(s[i] ==')'):
            arr[i+1] = -1
        else:
            arr[i+1] = 0
    for i in range(1,n+1):
        arr[i] = arr[i]+arr[i-1]
    p = ms(arr,0,n)
    print(p)
    q = (n*(n+1)//2)%1000000007
    #print((p*mi(q,1000000007))%1000000007)
