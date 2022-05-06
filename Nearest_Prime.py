t=int(input())
while t:
    a=int(input())
    for i in range(a,1,-1):
        for j in range(2,int(a**0.5)+1):
            if i%j==0:
                break
        else:
            r1=i
            break
    b=a
    while True:
        for j in range(2,int(a**0.5)+1):
            if a%j==0:
                break
        else:
            r2=a
            break
        a+=1
    if (abs(b-r1)>abs(r2-b)):
        print(r2)
    else:
        print(r1)
    t-=1

    