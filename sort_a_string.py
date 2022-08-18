s=input()
r=""
for i in s:
    if i.isalpha():
        r=r+i
r=sorted(r)
j=0
for i in s:
    if i.isalpha():
        print(r[j],end="")
        j+=1
    else:
        print(i,end="")