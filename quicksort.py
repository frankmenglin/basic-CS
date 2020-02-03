#define a function that merge two sorted list into one
def quicksort(A):
    if len(A)>1:
        pivot=len(A)-1
        L=[]
        R=[]
        for i in range (0,len(A)-1):
            if A[i]<A[pivot]:
                L=L+[A[i]]
            else:
                R=R+[A[i]]
        return quicksort(L)+[A[pivot]]+quicksort(R)
    else:
        return A
print(quicksort([1000,1,5,3,2322,6,8,9,53,4,3,2,43,1,2,4,5,7,8,32]))
