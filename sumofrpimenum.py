def sumofprimenum(n):
    sum = 0
    for i in range(2,n+1):
        j = 2
        count = 0
        while j < i:
            if i%j == 0:
                count += 1     
            j += 1
        if count == 0:
            sum += i
    return sum
            

if __name__ == "__main__":
    number = int(input())
    print(sumofprimenum(number))
