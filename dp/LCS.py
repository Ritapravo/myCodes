def subs(arr,s1, s2, n1, n2): 
  
    s = set() 
 
    if n1 == 0 or n2 == 0: 
        s.add("") 
        return s
  
    if s1[n1 - 1] == s2[n2 - 1]: 

        tmp = subs(arr,s1, s2, n1 - 1, n2 - 1) 
        for string in tmp: 
            s.add(string + s1[n1 - 1]) 

    else: 

        if arr[n1 - 1][n2] >= arr[n1][n2 - 1]: 
            s = subs(arr,s1, s2, n1 - 1, n2) 
            
        if arr[n1][n2 - 1] >= arr[n1 - 1][n2]: 
            tmp = subs(arr,s1, s2, n1, n2 - 1) 

            for i in tmp: 
                s.add(i) 
    return s

s1 = input()
s2 = input()
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
s = subs(arr,s1,s2,n1,n2)
for i in s:
    print(i)
