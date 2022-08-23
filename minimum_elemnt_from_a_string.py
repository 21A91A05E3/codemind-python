st=input()
w=st.split()
s=w[-1]
m=min(s)
for i in s:
    if ord(m)-ord(i)==-32:
        m=i
print(m)