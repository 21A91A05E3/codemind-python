s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
    print("True")
else:
    print("False")