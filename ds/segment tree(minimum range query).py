from sys import maxsize
from math import log,ceil

def getMid(s,e):
    return s + (e-s)//2

def constructST(arr,n):
    x = ceil(log(n,2))
    size = 2*pow(2,x)-1
    st = [0]*size
    sTree(arr,0,n-1,st,0)
    return st

def sTree(arr,ss,se,st,si):
    if(ss==se):
        st[si]=arr[ss] #if there is one element in an array,store it in current node
        return arr[ss]
    mid = getMid(ss,se)
    st[si]=min(sTree(arr,ss,mid,st,si*2+1),sTree(arr,mid+1,se,st,si*2+2))
    return st[si]


#st -> segment tree
#index -> index of current node in segment tree
#ss &se -> starting and ending indices of the segment represented by the current node
#qs &qe -> starting and ending indices of query range


def RMQtest(st,ss,se,qs,qe,index):
    if(qs<=ss and qe>=se):  #if the segment of this node is a part of
        return (st[index])  #the given range, then return min of the segment
    
    if(se<qs or ss>qe):     #if the segment of this node is outside the given range
        return maxsize
    mid = getMid(ss,se)
    # if a part of the segment overlaps with the given range
    return min(RMQtest(st,ss,mid,qs,qe,2*index+1),RMQtest(st,mid+1,se,qs,qe,2*index+2))

def RMQ(arr,n,qs,qe): 
    st=constructST(arr,n)
    if(qs<0 or qe>n-1 or qs>qe):
        print("error")
        return -1
    return RMQtest(st,0,n-1,qs,qe,0)

    


