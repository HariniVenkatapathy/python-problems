def combination(n,r):
    numer = 1
    d = n-r
    demon = 1
    ro = 1
    while n>0:
        numer = numer*n
        n -= 1
    while d>0:
        demon = demon*d
        d -= 1
    while r>0:
        ro = ro*r
        r -= 1
    deno = demon*ro
    last = numer//deno
    print(last)

if __name__ == "__main__":
    Number = int(input())
    R = int(input())
    combination(Number,R)
