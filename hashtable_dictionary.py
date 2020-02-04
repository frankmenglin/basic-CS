#python class basics

A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def H(x):
    return x%5

Table={}
for i in A:
    if H(i) in Table:
        Table[H(i)]=Table[H(i)]+[i]
    else:
        Table[H(i)]=[i]

print(Table)
