import sys
n = int(sys.stdin.readline())

s = []
for _ in range (n) : 
    c = sys.stdin.readline()
    cs = c.split()

    if cs[0] == "push" :
        s.append(cs[1])

    elif cs[0] == "top" :
        if(len(s)==0) : print(-1)
        else : print(s[len(s)-1])

    elif cs[0] == "size" :
        print(len(s))

    elif cs[0] == "empty": 
        if(len(s)==0) : print(1)
        else : print(0)

    elif cs[0] == "pop" :
        if(len(s)==0) : print(-1)
        else : print(s.pop())

