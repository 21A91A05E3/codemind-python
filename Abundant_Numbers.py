n=int(input())
fs=0
for i in range(1,n):
    if(n%i==0):
            fs=fs+i
if(fs>n):
    print("True")
else:
    print("False")