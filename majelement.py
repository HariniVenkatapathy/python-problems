def majorityele(arr):
    rule = len(arr)//2
    temp = len(arr)
    maj = 0
    majcount = 0
    i = 0
    while temp>0:
        tempo = arr.count(i)
        if tempo>majcount and i!=maj:
            majcount = tempo
            maj = i
        temp -= 1
        i += 1
    if arr.count(maj)>rule:
        print(maj)
    else:
        print(-1)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    majorityele(arr)
                
