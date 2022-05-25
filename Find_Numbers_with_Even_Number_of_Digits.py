t=int(input())
a=list(map(int,input().split()))
ec=0
for i in a:
    c=0
    while(i):
        d=i%10
        i=i//10
        c+=1
    if(c%2==0):
        ec+=1
print(ec)