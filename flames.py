def Flames(n1,n2):
    result = ""
    seen = list(n1)
    for i in range(len(n2)):
        if n2[i] in seen:
            seen.remove(n2[i])
        else:
            seen.append(n2[i])
    print(seen)
    count = len(seen)
    print(count)
    l = ['F','L','A','M','E','S']
    index = 0
    while len(l)>1:
        index = (index+count-1)%len(l) #the only thing i didnt know how to do is rotate the array
        l.pop(index)
    result_map = {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }
    print( result_map[l[0]])
        
        
                   

if __name__ == "__main__":
    n1 = input()
    n2 = input()
    Flames(n1,n2)
                
