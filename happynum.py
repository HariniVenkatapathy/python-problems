def happynum(n):
    seen = set()
    while n!=1 and n not in seen:
        seen.add(n)
        sq = 0
        while n>0:
            dig = n%10
            sq += dig * dig
            n = n//10
        n = sq
        
    return n == 1
    

if __name__ == "__main__":
    number = int(input())
    if happynum(number):
        print("happy number")
    else:
        print("unhappy number")
