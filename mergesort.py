#define a function that merge two sorted list into one
def merge(A,B):
    C=[]
    for i in range (len(A)+len(B)):
        if len(A)==0:
            C=C+[B[0]]
            B.pop(0)
        elif len(B)==0:
            C=C+[A[0]]
            A.pop(0)
        elif A[0]<B[0]:
            C=C+[A[0]]
            A.pop(0)
        else:
            C=C+[B[0]]
            B.pop(0)
    return C

def mergesort(A):
    if len(A)>1:
        mid=(len(A)+1)//2
        L=mergesort(A[:mid])
        R=mergesort(A[mid:])
        return merge(L,R)
    else:
        return A
print(mergesort([100,1,5,3,2,6,8,9,5,4,3,2,43,1,2,4,5,7,8,32]))