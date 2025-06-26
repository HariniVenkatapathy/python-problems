def closest(n,m):
    if n<0:
        n =-n
    num = n
    addo = 0
    subo = 0
    for i in range(m):
        add = num+1
        if add%m == 0:
            addo = add
        sub = num-1
        if sub%m == 0:
            subo = sub
    a = n-addo
    s = abs(n-subo)
    if a<s:
        if n<0:
            print(-addo)
        else:
            print(addo)
    else:
        if n<0:
            print(-subo)
        else:
            print(subo)
        

if __name__ == "__main__":
    Number  = int(input())
    M = int(input())
    print(closest(Number,M))
