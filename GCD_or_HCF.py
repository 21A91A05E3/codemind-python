a,b=map(int,input().split())
h=0
i=1
while(i<=a and i<=b):
        if(a%i==0 and b%i==0):
            h=i
        i+=1
print(h)
