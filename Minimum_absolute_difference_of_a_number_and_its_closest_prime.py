a=int(input())
for i in range(a,1,-1):
    for j in range(2,int(a**0.5)+1):
        if i%j==0:
            break
    else:
        break
b=a
while True:
    for j in range(2,int(a**0.5)+1):
        if a%j==0:
            break
    else:
        break
    a+=1
if (abs(b-i)>abs(a-b)):
    print(abs(a-b))
else:
    print(abs(b-i))