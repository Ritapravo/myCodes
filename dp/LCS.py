"""
Input:
abcdafe
abdcef

Output:
4
{'abdf', 'abcf', 'abde', 'abce'}

"""
def reverse(s):
    s2 = ""
    n = len(s)
    for i in range(n-1,-1, -1):
        s2 = s2 + s[i]
    return (s2)

def lcs(arr,s1, s2, m, n, curr, l):
    if(n == 0 or m==0):
        l.add(curr)
        return
    if(s1[m-1] == s2[n-1]):
        lcs(arr, s1, s2, m-1 , n-1, curr+s1[m-1], l)
    else:
        if(arr[m][n]==arr[m-1][n]):
            lcs(arr, s1, s2, m-1, n, curr, l)
            
        if(arr[m][n]==arr[m][n-1]):
            lcs(arr, s1, s2, m, n-1, curr, l)

            
s1 = reverse(input())
s2 = reverse(input())
n1 = len(s1)
n2 = len(s2)

arr = [[0 for i in range(n2+1)] for j in range(n1+1)]
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if(s1[i-1]==s2[j-1]):
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j],arr[i][j-1])
print(arr[n1][n2])

l = set()
curr = ""
lcs(arr, s1, s2, n1, n2, curr, l)
print(l)
