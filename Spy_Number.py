n=int(input())
sum=0
pro=1
while (n):
    d=n%10
    sum=sum+d
    pro=pro*d
    n=n//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")
