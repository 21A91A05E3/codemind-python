st=input()
sum=0
i=1
for i in st:
    if(i.isnumeric()):
        sum=sum+int(i)
print(sum)