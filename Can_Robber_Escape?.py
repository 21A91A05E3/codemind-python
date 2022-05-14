n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if(a[i]%2):
        c+=1
if(c<=2):
    print("YES")
else:
    print("NO")