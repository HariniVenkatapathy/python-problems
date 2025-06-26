def ap(a1,a2,n):
    d = a2 - a1
    temp = a2
    pos = 2
    while pos<n:
        temp = temp+d
        pos+=1
    return temp

if __name__ == "__main__":
    A1 = int(input())
    A2 = int(input())
    Number = int(input())
    print(ap(A1,A2,Number))
