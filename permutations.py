def permutation(n,r):
    numer = 1
    d = n-r
    denom = 1
    while n>0:
        numer = numer*n
        n -= 1
    while d>0:
        denom = denom*d
        d -= 1
    last = numer//denom
    print(last)

if __name__ == "__main__":
    number = int(input())
    R = int(input())
    permutation(number,R)
