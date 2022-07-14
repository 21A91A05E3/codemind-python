s=input()
w=s.split()
for i in range(len(w)):
    if i%2==0:
        t=w[i]
        print(t[::-1],end=" ")
    else:
        print(w[i],end=" ")