a=int(input())
b=int(input())
sum=0
c=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum==b):
    c+=1
sum=0
for i in range(1,b):
    if(b%i==0):
        sum=sum+i
if(sum==a):
    c+=1
if(c==2):
    print("Amicable")
else:
    print("Not Amicable")