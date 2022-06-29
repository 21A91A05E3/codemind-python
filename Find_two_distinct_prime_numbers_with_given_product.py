def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=0
b=0
c=0
for i in range(2,n//2+1):
    if(p(i)==1 and n%i==0):
        a=i
        r=n//i
        if(p(r)):
            c+=1
            b=r
if(c==0):
    print(-1)
else:
    print(b,a)