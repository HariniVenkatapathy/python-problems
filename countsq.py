def perfectsq(n):
    for i in range(1,n):
        sq = i*i
        if sq<n:
            print(sq)
        else:
            break
    
        

if __name__ == "__main__":
    number = int(input())
    perfectsq(number)
