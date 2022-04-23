n=int(input())
t=n
sum=0
while n:
    d=n%10
    sum=sum+d
    n=n//10
if(t%sum==0):
    print("True")
else:
    print("False")