#reverse the first k elements of queue

def Queuereverse(A):
    if len(A)==0:
        return []
    else:
        B=[]
        B.insert(0,A[-1])
        A.pop()
        A=Queuereverse(A)
        A.insert(0,B[-1])
    return A

def reversefirstk(A,k):
    l=len(A)
    if l<=k:
        return Queuereverse(A)
    else:
        B=[]
        for i in range (l-k):
            B.insert(0,A[-1])
            A.pop()
        A=Queuereverse(A)
        for i in range (k):
            B.insert(0,A[-1])
            A.pop()
    return B


A=[3,5,6,3,2,7,5,4,14,8,12,32]
print(reversefirstk(A,5))

