def nosq(a,b):
    totsq = 0
    while a>0 and b>0:
        totsq += a*b
        a -= 1
        b -= 1
    return totsq

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    print(nosq(A,B))
