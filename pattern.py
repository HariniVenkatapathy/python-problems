def pattern(n):
    for i in range(n):
        for j in range(n,0,-1): #in python to lopp from high to low  use -1
            for _ in range(n-i): 
                print(j,end =" ")
        print("-1")

if __name__ == "__main__":
    number = int(input())
    pattern(number)
                
            
