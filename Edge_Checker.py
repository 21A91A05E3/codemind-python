a,b=map(int,input().split())
if abs(a-b)==1:
    print("Yes")
elif a==1 and b==10:
    print("Yes")
elif abs(b-a)==1:
    print("Yes")
elif b==1 and a==10:
    print("Yes")
else:
    print("No")