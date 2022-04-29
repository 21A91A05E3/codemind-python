import math
t=int(input())
while(t>0):
    c=0
    st=input()
    for i in st:
        if(i.isnumeric()):
            c+=1
    if(c!=0):
        print("Yes")
    else:
        print("No")
    t=t-1