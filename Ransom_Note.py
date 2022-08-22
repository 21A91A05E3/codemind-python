def rn(s1,s2):
    c=0
    for i in s1:
        if i in s2:
            s2.remove(i)
        else:
            return False
    return True

s1,s2=map(str,input().split())
s2=list(s2)
print(rn(s1,s2))