n=int(input())
t=n
sum=0
while n:
    d=n%10
    fact=1
    for i in range (1,d+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(t==sum):
    print('The number' ,t, 'is a strong number')
else:
    print('The number' ,t, 'is not a strong number')
    

    
    