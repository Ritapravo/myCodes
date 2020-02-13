
# 0/1 Knapsack Problem 

w = int(input())
weight = [int(i) for i in input().split()]
values = [int(i) for i in input().split()]

n = len(values)
arr = [[0 for i in range(w+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,w+1):
        if(j<weight[i-1]):
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j],arr[i-1][j-weight[i-1]]+values[i-1])
#print(arr)
x = arr[n][w]
print("maximum value = ",x)
i = n
j = w
print("Weights taken:",end = " ")
while(arr[i][j]>0):
    if(arr[i][j]==arr[i-1][j]):
        i = i-1
    else:
        print(weight[i-1],end = " ")
        j = j-weight[i-1]
        i = i-1
        
    #print(i,j)

