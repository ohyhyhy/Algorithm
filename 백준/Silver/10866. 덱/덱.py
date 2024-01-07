import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()

for _ in range(N) :
    c = sys.stdin.readline().split()
    
    if c[0] == 'push_front' :
        q.appendleft(c[1])
    elif c[0] == 'push_back' :
        q.append(c[1])
    elif c[0] == 'pop_front' :
        if q : print(q.popleft())
        else : print(-1)
    elif c[0] == 'pop_back' :
        if q : print(q.pop())
        else : print(-1)
    elif c[0] == 'size' :
        print(len(q))
    elif c[0] == 'empty' :
        if q : print(0)
        else : print(1)
    elif c[0] == 'front' :
        if q : print(q[0])
        else : print(-1)
    elif c[0] == 'back' :
        if q : print(q[len(q)-1])
        else : print(-1)

