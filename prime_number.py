n=int(input())
c=0
for i in range(n):
    if(n%(i+1)==0):
        c+=1
if(c==2):
    print("prime")
else:
    print("not a prime")