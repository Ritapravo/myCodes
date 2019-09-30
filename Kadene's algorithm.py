def max_subarray_sum(arr,size):
    m=0 #stores max
    c=0 #stores current max
    for i in range(size):
        c=max(arr[i],c+arr[i])
        m=max(c,m)
        print(c)
    return m
