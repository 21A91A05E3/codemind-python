n=int(input())
ec=0
c=0
dc=0
while n>0:
    d=n%10
    if(d%2==0):
        ec+=1
    if(d%2==1):
        dc+=1
    n=n//10
    c+=1
if(c==ec):
    print("Even")
elif(c==dc):
    print("Odd")
else:
    print("Mixed")