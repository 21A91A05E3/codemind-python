t=int(input())
for i in range(t):
    s=input()
    c=0
    for i in range(0,len(s)):
        if(s[i].isnumeric()):
            c+=1
    if(c==len(s)):
        print("True")
    else:
        print("False")
    
