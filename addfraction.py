def frac(n1,d1,n2,d2):
    if d1 == d2:
        addo = n1+n2
        print(f"{addo}/{d1}")
    

if __name__ == "__main__":
    N1 = int(input())
    D1 = int(input())
    N2 = int(input())
    D2 = int(input())
    frac(N1,D1,N2,D2)
