import sys
import copy

input = sys.stdin.readline

N = int(input())

sonnim=[]
new=[] 
tip=0
order=1

for _ in range(N):
    temp = int(input())
    sonnim.append(temp)

sonnim.sort(reverse=True) 

for i in sonnim: 
    sum=i-(order-1)
    if(sum>0):
        tip+=sum
    order+=1
 
print(tip)