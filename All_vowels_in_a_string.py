s=input()
r=set(s)
s=str(r)
c1=0
c2=0
for i in s:
    if i in 'aeiou':
        c1+=1
for i in s:
    if i in 'AEIOU':
        c2+=1
if c1>=5 or c2>=5:
    print("True")
else:
    print("False")