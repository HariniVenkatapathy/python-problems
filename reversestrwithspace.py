def reversestrwithspace(word):
    word = word+ " "
    i = 0
    j = len(word)-1
    chars = list(word)
    while i<j:
        if chars[i] == ' ': #update and check i and j seperately
            i += 1
        elif chars[j] == ' ':
            j -= 1
        else:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
    return ''.join(chars)

    

if __name__ == "__main__":
    word = input()
    print(reversestrwithspace(word))
