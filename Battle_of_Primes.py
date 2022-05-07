a=int(input())
b=int(input())
s=a+b
for i in range(1,10):
    r=s+i
    c=0
    for j in range(1,r+1):
        if(r%j==0):
            c+=1
    if(c==2):
        print(j-s)
        break
    