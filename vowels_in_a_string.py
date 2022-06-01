s=input()
k=input()
c=0
if k in s:
    c+=1
    print("True")
    print(s.index(k))
    
if(c==0):
    print("False")