n=int(input())
b=bin(n)
b=b[2:]
b=list(b)
for i in range(len(b)):
    if b[i]=="1":
        b[i]="0"
    else:
        b[i]="1"
b="".join(b)   
r=int(b,2)
print(r)