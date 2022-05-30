def p(x):
    t=x
    r=0
    while(x):
        d=x%10
        r=r*10+d
        x=x//10
    if(r==t):
        return 1
    else:
        return 0
n=int(input())
a=n-10
b=n+10
c=0
d=0
for i in range(a,n):
    if(p(i)):
        c=i
        break
for j in range(b,n-1,-1):
    if(p(j)):
        d=j
        break
if(abs(n-c)>abs(n-d)):
    print(d)
elif(abs(n-c)==abs(n-d)):
    print(c,d)
else:
    print(c)
            
            
    