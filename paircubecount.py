def paircubecount(n):
    a =1
    count = 0
    while a**3 < n: 
        b3 = n - a**3
        b = round(b3 ** (1/3))
        if b >= 0 and b**3 == b3:
            count += 1
        a += 1
    return count

if __name__ == "__main__":
    number = int(input())
    print(paircubecount(number))
