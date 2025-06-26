def perfectnum(n):
    sum = 0
    for i in range(1,n-1):
        if n%i == 0:
            sum += i
    if sum == n:
        print("the given number is a perfect number")
    else:
        print("the given number is not perfect number")

if __name__ == "__main__":
    Number  = int(input())
    perfectnum(Number)
