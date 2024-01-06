import sys
from collections import deque
T = int(sys.stdin.readline().strip())
 
q = deque([])

for _ in range(T) : 
    c = sys.stdin.readline().split()
 
    if c[0] == "push" :
        q.append(c[1])
    elif c[0] == "pop" :
        if q : print(q.popleft())
        else : print(-1)
    elif c[0] == "size" :
        print(len(q))
    elif c[0] == "empty" :
        if(len(q)) : print(0)
        else : print(1)
    elif c[0] == "front" :
        if(len(q)) : print(q[0])
        else : print(-1)
    elif c[0] == "back" :
        if(len(q)) : print(q[-1])
        else : print(-1)
