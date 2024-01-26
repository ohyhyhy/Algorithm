import sys
import copy

input = sys.stdin.readline

N = int(input())

rope=[]
new=[]
weight=[]
max=0
for _ in range(N):
    temp = int(input())
    rope.append(temp)

new=sorted(rope)
sorted(new)
 
for i in copy.deepcopy(new):
    weight.append(i*len(new)) 
    new.remove(i)
     

for i in weight:
    if max<i:
        max=i

print(max)