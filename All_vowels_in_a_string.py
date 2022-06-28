s=input()
s.lower()
r=""
for i in s:
    if i in 'aeiou':
        if i not in r:
            r=r+i
if(len(r)==5):
    print("True")
else:
    print("False")