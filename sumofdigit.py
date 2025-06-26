def sumofdigit(n):
     sumo = 0
     while n>0:
         dig = n%10
         sumo += dig
         n = n//10
     return sumo

if __name__ == "__main__":
    num = int(input())
    print(sumofdigit(num))
