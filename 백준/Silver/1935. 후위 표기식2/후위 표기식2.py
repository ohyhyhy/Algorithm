N = int(input())

l = input()
num = [0]*N
stack = []

for i in range(N) :
    num[i] = int(input())

for i in l :
    if 'A' <= i <= 'Z' :
        stack.append(num[ord(i)-ord('A')])
    else:
        op2 = stack.pop()
        op1 = stack.pop()

        if i=="+" :
            stack.append(op1+op2)
        elif i == "-" :
            stack.append(op1-op2)
        elif i == "*" :
            stack.append(op1*op2)
        elif i == "/" :
            stack.append(op1/op2)

print('%.2f' %stack[0])
