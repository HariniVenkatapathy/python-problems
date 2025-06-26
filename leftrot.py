def leftrot(num,r):
    n = num
    dig = num%10
    count = 0
    no = 1
    while n>0:
        count += 1
        n //= 10
    while count>1:
        no *= 10
        count -= 1
    num -= dig
    num *= no*10*dig
    print(num)

if
    
