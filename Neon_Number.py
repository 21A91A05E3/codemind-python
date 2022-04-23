n=int(input())
s=n*n
sum=0
while s:
    d=s%10
    sum=sum+d
    s=s//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    
    