s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
w1=s1.split()
w2=s2.split()
c=0
for i in w1:
    if i in w2:
        if(w1.count(i)==1):
            if(w2.count(i)==1):
                c+=1
print(c)