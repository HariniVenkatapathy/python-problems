import math

def factors(n):
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(1, sqrt_n):
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:
                print(n // i, end=" ")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    factors(num)
