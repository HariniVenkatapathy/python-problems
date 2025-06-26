def largestprime(n):
    d = 2
    while d * d <= n:
        if n%d == 0:
            n = n//d
        else:
            d+=1
    print(d)

if __name__ == "__main__":
    Number = int(input())
    largestprime(Number)
            
        
