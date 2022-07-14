alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def num(n):
    if n< 26:
        return alpha[n-1]
    else:
        q, r = n//26, n% 26
        if r == 0:
            if q == 1:
                return alpha[r-1]
            else:
                return num(q-1) + alpha[r-1]
        else:
            return num(q) + alpha[r-1]
n=int(input())
print(num(n))