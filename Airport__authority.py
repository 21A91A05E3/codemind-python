n=int(input())
w=[]
for i in range(n):
    a=int(input())
    w.append(a)
t=int(input())
b=0
c=0
for i in range(n):
    if(w[i]>t):
        b=b+2
    else:
        c=c+1
print(b+c)