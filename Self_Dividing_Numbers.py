a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    sd=0
    dc=0
    while i:
        d=i%10
        if(d!=0 and t%d==0):
            sd+=1
        i=i//10
        dc+=1
    if(dc==sd):
        print(t,end=' ')
    