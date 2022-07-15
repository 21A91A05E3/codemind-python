n=int(input())
l=list(map(int,input().split()))
r=int(input())
c=0
for j in l:
    if j==r:
        c+=1
        break
if(c):
    print("True")
else:
    print("False")