def ct(c):
    r= ""
    while c> 0:
        r= chr(ord('A') + (c-1) % 26) + r
        c=(c- 1) // 26
    return r
n=int(input())
a=ct(n)
print(a)