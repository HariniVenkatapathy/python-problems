def uniqueinarr(arr):
    num = set(arr)
    ans = [i for i in num if not arr.count(i)>1]
    print(ans[0])        
            

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    uniqueinarr(arr)
            
