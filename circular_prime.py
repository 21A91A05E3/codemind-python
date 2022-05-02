n=int(input())
c=0
pc=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    r=0
    while(n>0):
        d=n%10
        r=(r*10)+d
        n=n//10
    for i in range(1,r+1):
        if(r%i==0):
            pc+=1
    if(pc==2):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        

