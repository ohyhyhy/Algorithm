import sys

A, B = map(int,input().split(" "))

sumA=A
sumB=B

if(A>B) :
    m = B
else :
    m = A

for i in range (1,m+1):
    if(A%i==0 and B%i==0) :
        max = i

while 1:
    if(sumA>sumB) :
        sumB+=B
    elif(sumB>sumA) :
        sumA+=A
    else:
        break

print(max)
print(sumA)

