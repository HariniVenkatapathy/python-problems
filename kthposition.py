def kthpos(a,b,n):
    num = pow(a,b)
    rev = 0
    pos = 1
    dig = 1
    while pos<=n and num>0:
        dig = num%10
        num = num//10
        pos+=1
    return dig

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    N = int(input())
    print(kthpos(A,B,N))
    
        
        
