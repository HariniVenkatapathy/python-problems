def rev(n):
    rev = 0
    while n>0:
        dig = n%10
        rev = (rev+dig)*10
        n = n//10
    return rev//10

if __name__ == "__main__":
    number = int(input())
    print(rev(number))
