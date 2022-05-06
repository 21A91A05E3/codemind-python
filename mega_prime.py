n=int(input())
c=0
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print("Not Mega Prime")
        break
else:
    p=0
    dc=0
    while(n>0):
        c=0
        d=n%10
        dc+=1
        for j in range(1,d+1):
            if d%j==0:
                c+=1
        if(c==2):
            p+=1
        n=n//10
if(p==dc):
    print("Mega Prime")
else:
    print("Not Mega Prime")

