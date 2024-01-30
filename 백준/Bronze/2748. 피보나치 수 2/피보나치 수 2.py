n=int(input())
arr=[-1]*(n+1)
arr[0]=0
arr[1]=1

def fibo(n):
    if arr[n]!=-1: 
        return arr[n]

    arr[n]=fibo(n-2)+fibo(n-1)
    return arr[n]

print(fibo(n))