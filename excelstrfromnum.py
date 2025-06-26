def excel(n):
    if n<27:
        n += 64
        letter = chr(n)
        print(letter)
    else:
        result = ""
        while n>0:
            n -= 1 # to get 0 when 51%26 which is 0+65 is A
            result = chr(n % 26 + 65) + result
            n //= 26
        print(result)
            

if __name__ == "__main__":
    number = int(input())
    excel(number)
    
