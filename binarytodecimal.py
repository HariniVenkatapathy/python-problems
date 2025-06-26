def bintodeci(num):
    n = num
    count = 0
    tot = 0
    while n>0:
        dig = n%10
        if dig == 1:
            tot += pow(2,count)
        count += 1
        n = n//10
    return tot

if __name__ == "__main__":
    number = int(input())
    print(bintodeci(number))
