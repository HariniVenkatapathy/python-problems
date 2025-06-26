def armstrong(n):
    org = n
    num = n
    sumo = 0
    count = 0
    while num>0:
        temp = num%10
        num = num//10
        count+=1
    while n>0:
        digit = n%10
        sumo += pow(digit,count)
        n = n//10
    return sumo

if __name__ == "__main__":
    number = int(input())
    nummy = armstrong(number)
    if number == nummy:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")
