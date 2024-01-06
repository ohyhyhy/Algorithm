T = int(input())
 

for _ in range(T) : 
    s=[]
    c = input()

    for i in c :
        if(i == '(') :
            s.append(i)
        elif(i == ')') : 
            if s : 
                s.pop()
            else :
                print('NO')
                break

    else :
        if s:
            print('NO')
        else :
            print('YES')

