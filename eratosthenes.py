def eratosthenes(n):
    for i in range(2,n):
        j = 2
        count = 0
        while j < i:
            if i%j == 0:
                count += 1     
            j += 1
        if count == 0:
            print(i)

if __name__ == "__main__":
    number = int(input())
    eratosthenes(number)
                    
