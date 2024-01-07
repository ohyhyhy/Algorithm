import sys
from collections import deque
N = int(sys.stdin.readline().strip())
 
q = deque([])

for i in range(N) :
    i+=1
    q.append(i)
 
while len(q) != 1 :
    q.popleft()
    q.append(q.popleft())

print(q[0])