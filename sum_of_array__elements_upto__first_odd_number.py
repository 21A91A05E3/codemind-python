n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
    if i%2==1:
        break
    else:
        c+=i
print(c)