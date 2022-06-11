l=list(map(int,input().split(',')))
r=[]
for i in l:
    sum=0
    c=0
    for j in range(1,i+1):
        if i%j==0:
            sum=sum+j
    for k in l:
        if sum==k:
            c+=1
            break
    if(c):
        r.append(i)
if(len(r)):
    print(*(sorted(r)))
else:
    print("-1")


        