def countsmallarr(x,arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]<=x:
            count += 1
    print(count)

if __name__ == "__main__":
    x = int(input())
    arr = list(map(int,input().split()))
    countsmallarr(x,arr)
