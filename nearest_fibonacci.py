n=int(input())
if(n==0):
    print(0)
a= 0
b= 1
sum=a+b
while(sum<=n):
    a=b
    b=sum
    sum=a+b
if (abs(sum-n)>abs(b-n)):
    r=b
elif(abs(sum-n)==abs(b-n)):
    print(b,sum)
else:
    r=sum
print(r)