n=int(input())
c=0
for i in range(n):
    if(i*(i+1)==n):
        c+=1
if(c!=0):
    print("YES")

else:
    print("NO")