def Gp(a,r,n):
    temp = a
    pos = 2
    while pos<=n:
        temp = temp*r
        pos+=1
    return temp

if __name__ == "__main__":
    A = int(input())
    R = int(input())
    Num = int(input())
    print(Gp(A,R,Num))
