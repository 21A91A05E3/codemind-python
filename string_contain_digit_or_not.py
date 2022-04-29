import math
st=input()
c=0
for i in st:
    if(i.isnumeric()):
        c+=1
if(c!=0):
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")
