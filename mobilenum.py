def mobnum(number):
    num = ['0','1','2','3','4','5','6','7','8','9']
    words = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    count = 0
    for c in number:
        for i in range(10):
            if c == num[i]:
                print(words[i], end =" ")
            

if __name__ == "__main__":
    NUM = str(input())
    mobnum(NUM)
                
            

                
