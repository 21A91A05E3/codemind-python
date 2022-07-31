h,m=map(int,input().split(':'))
a=abs(h*30-(11*m)/2)
if a<(360-a):
    if a>=int(a):
        print(a)
else:
    print(360-a)