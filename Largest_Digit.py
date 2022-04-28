n=int(input())
max=0
while n>0:
    d=n%10
    if(max<d):
        max=d
    n=n//10
print(max)
    