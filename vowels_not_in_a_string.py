s=input()
c=0
for i in 'aeiou':
    if i not in s:
        c+=1
        print(i,end=" ")
if(c==0):
    print("0")