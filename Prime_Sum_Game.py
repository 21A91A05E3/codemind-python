def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a,b,c,d=map(int,input().split())
h=0
for i in range(a,b+1):
    h=0
    for j in range(c,d+1):
        if(p(i+j)):
            h+=1
    if h==0:
        print("Takahashi")
        break
else:
    print("Aoki")