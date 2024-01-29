arr=[]
cnt=0
string=input()
str=""
idx=0

#l=list(string)
#l=['B' if x=='X' else 'X' for x in l]

for i in list(string):
    if i=='X':
        cnt+=1

        if cnt%4==0:
            cnt-=4
            arr.append("AAAA")

    elif i==".":
        if cnt%2==1: 
            idx=1
            break
        elif cnt!=0 and cnt%2==0:
            arr.append('BB.')
            cnt=0
        else:
            arr.append('.')
            cnt=0

    

if idx==1 or cnt%2==1:
    print(-1)
elif cnt!=0 and cnt%2==0:
    for i in arr:
        str+=i
    str+="BB"    
    print(str)

else:
    for i in arr:
        str+=i
    print(str)