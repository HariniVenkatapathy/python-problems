def prime(n):
    i = 2
    count = 0
    while i<=n:
        if n%i == 0:
            if i !=n:
                count += 1
        i += 1
    if count==0:
        print("True")
    else:
        print("false")

if __name__ == "__main__":
    number = int(input())
    prime(number)
    
