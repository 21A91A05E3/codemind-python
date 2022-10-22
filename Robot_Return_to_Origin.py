s=input()
h=0
v=0
for i in s:
    if i=="L":
        h+=1
    elif i=="R":
        h-=1
    elif i=="U":
        v+=1
    else:
        v-=1
if(h==0 and v==0):
    print("True")
else:
    print("False")