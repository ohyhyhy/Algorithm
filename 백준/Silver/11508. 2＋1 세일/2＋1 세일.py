N = int(input())

arr=[]
sum=0

for _ in range(N):
    t=int(input())
    arr.append(t)

arr.sort(reverse=True)

for i in range(N):
    if i%3==0:
        sum+=arr[i]
    elif i%3==1:
        sum+=arr[i]

print(sum)