n,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
s=0
for i in l:
    if i<=d and s<=1:
        c+=1
    else:
        s+=1
print(c)
           
        
    
    