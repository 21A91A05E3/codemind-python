s=input()
cb=s.count('b')
ca=s.count('a')
cl=s.count('l')
co=s.count('o')
cn=s.count('n')
m=min(cb,ca,cl//2,co//2,cn)
if cb==0 or ca==0 or cl==0 or co==0 or cn==0:
    print(0)
else:
    print(m)