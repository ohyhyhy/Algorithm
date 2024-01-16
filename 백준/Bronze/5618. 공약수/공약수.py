import sys

T = int(sys.stdin.readline())

if T==2:
    a,b = (map(int, sys.stdin.readline().split()))
    m = min(a,b)
    for i in range(1,m+1):
        if(a%i==0 and b%i==0) :
            print(i)
elif T==3:
    a,b,c = (map(int, sys.stdin.readline().split()))
    m = min(a,b,c)
    for i in range(1,m+1):
        if(a%i==0 and b%i==0 and c%i==0) :
            print(i)
