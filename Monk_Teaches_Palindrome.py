t=int(input())
while(t):
    s=input()
    r=s[::-1]
    if(r==s):
        if(len(s)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    t=-1