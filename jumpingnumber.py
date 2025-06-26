def jumpinnum(n):
    temp = n
    org = n
    while temp>0:
        num = str(temp)
        count = len(num)
        numb = temp
        pairs = 0
        jump = False
        while numb>=10:  #to avoid zeros in subo and addo , we keep the limit from 10
            temp1 = numb%10
            numb = numb//10
            temp2 = numb%10
            addo = temp1+1
            subo =  temp1-1
            if addo == temp2 or subo == temp2:
                pairs += 1
            else:
                break
        if count == pairs+1:
            if temp == org:
                print("the given number is jumping number")
            else:
                print(f"No, the jumping numbe before the given number is :{temp}")
            break
        else:
            temp-=1
            

if __name__ == "__main__":
    number = int(input())
    jumpinnum(number)
