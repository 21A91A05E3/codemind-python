n=int(input())
c=0
for i in range(n//2):
    if(i*i==n):
        c+=1
if(c!=0):
    print("True")
else:
    print("False")