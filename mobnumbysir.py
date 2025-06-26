def mobnum(number):
    words = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    count = 1
    number = number + " "
    for i in range(len(number)-1):
        if number[i] == number[i+1]:
            count += 1
        else:
            digit = int(number[i])
            if count == 2:
                print(f"Double {words[digit]}")
            elif count == 3:
                print(f"Triple {words[digit]}")
            elif count == 4:
                print(f"Double {words[digit]} Double {words[digit]}")
            elif count == 5:
                print(f"Triple {words[digit]} Double {words[digit]}")
            elif count == 6:
                print(f"Triple {words[digit]} Triple {words[digit]}")
            else:
                print(words[digit])
            count = 1
    


if __name__ == "__main__":
    NUM = input()
    mobnum(NUM)
