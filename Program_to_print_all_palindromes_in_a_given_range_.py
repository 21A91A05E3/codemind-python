a=int(input())
b=int(input())
r=0
for i in range(a,b+1):
    t=i
    while i>0:
        d=i%10
        r=(r*10)+d
        i=i//10
    if(r==t):
        print(t,end=' ')
    r=0
        