n=int(input())
sum=0
pro=1
while (n):
    d=n%10
    sum=sum+d
    pro=pro*d
    n=n//10
print(pro-sum)
