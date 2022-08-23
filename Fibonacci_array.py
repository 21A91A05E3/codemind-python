n=int(input())
l=list(map(int,input().split()))
c=0
if len(l)<=2:
    print("no")
else:
    for i in range(2,len(l)):
        if l[i-2]+l[i-1]==l[i]:
            c+=1
    if c==len(l)-2:
        print("yes")
    else:
        print("no")