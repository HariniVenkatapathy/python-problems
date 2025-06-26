def rightrot(num,r):
    while r>0: #optimize this dude 
        n = num
        count = 0
        no = 1
        dig = 0
        while num>0:
            dig = num%10
            num //= 10
            count += 1    
        while count>1:
            no *= 10
            count -= 1
        no *= dig
        n -= no
        n *= 10
        n += dig
        num = n
        r -= 1
    print(num)

if __name__ == "__main__":
    number = int(input())
    rotation = int(input())
    rightrot(number,rotation)
