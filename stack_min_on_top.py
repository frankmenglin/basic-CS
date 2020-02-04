#given a stack, create a stack that put minimum on top (so getmin has time complexity O(1))
A=[3,5,6,3,2,7,5,4,14,8,12,32]
B=[]
for i in range (len(A)):
    if len(B)==0:
        B.append(A[-1])
        A.pop()
    elif A[-1]<B[-1]:
        B.append(A[-1])
        A.pop()
    else:
        A.pop()
print(B[-1])

