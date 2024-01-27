import sys
import copy

N = int(input())

sonnim=[]

time=0
sonnim=list(map(int,input().split()))

sonnim.sort(reverse=False)  

for i in range(N): 
    sum=0
    for j in range(i+1):
        sum+=sonnim[j]
    time+=sum
 
print(time)