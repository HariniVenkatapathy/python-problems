def noofrec(a,b):
    totrec = 0
    for i in range(a,0,-1):
        for j in range(b,0,-1):
            temp = i*j                 #can add the number of iteration of row and column and multipy it
            totrec += temp
    return totrec

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    print(noofrec(A,B))
    
#to avoid time limit exceed use this formula [(m*(m+1)/2)*(n*(n+1)/2)]
