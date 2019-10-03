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
        
