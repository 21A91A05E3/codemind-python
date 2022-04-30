t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    if(a%b==0):
        c=n/b-n/a
    elif(b%a==0):
        c=n/a-n/b
    else:
        c=n/a+n/b-2*(n/(a*b))
    if(c>=k):
        print("Win")
    else:
        print("Lose")
