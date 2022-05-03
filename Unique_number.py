n=int(input())
l=list()
c=0
while n:
    r=n%10
    l.append(r)
    n=n//10
for i in l:
    if l.count(i)>1:
        c+=1
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")