t=int(input())
while(t>0):
    c=0
    n=int(input())
    for i in range(1,n):
        if(i*i==n):
            c+=1
    if(c!=0):
        print("True")
    else:
        print("False")
    t=t-1