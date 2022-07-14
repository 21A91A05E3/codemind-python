s=input()
l=list(s)
i=0
j=len(s)-1
while(i<j):
    if l[i] not in 'aeiouAEIOU':
        i+=1
    elif l[j] not in 'aeiouAEIOU':
        j-=1
    else:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
print("".join(l))