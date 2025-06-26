def sortedsq(arr):
    seq = False
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                for k in range(j+1,len(arr)):
                    if arr[i]<arr[j]<arr[k]:
                        print(1)
                        seq = True
    if seq == False:
        print(0)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    sortedsq(arr)
