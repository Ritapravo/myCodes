def ps2(arr,y, m, n, curr, l):
    if(n == 0):
        l.append(curr)
        return
    if(arr[m-1][n]==True):
        ps2(arr, y, m-1, n, curr,l)
    
    if(arr[m-1][n-y[m-1]]==True and n-y[m-1]>=0):
        ps2(arr, y, m-1, n-y[m-1], curr+[y[m-1]],l)

x = 1
y = [2, 3, 7, 8, 10]
m = len(y)
n = x
arr = [[False for j in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    arr[i][0] = True
for i in range(1,m+1):
    for j in range(1,n+1):
        if(j<y[i-1]):
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = arr[i-1][j] | arr[i-1][j-y[i-1]]
            
i = m
j = n

if(arr[i][j]==True):
    print("Yes")
    l = list()
    curr = []
    ps2(arr, y, m, n, curr, l)
    print(l)
else:
    print("NO")
