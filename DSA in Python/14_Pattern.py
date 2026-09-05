"""

      A       
    A B A     
  A B C B A   
A B C D C B A 

"""

def printPattern(rows , cols):
    for i in range(rows):
        char = ord('A') - 1
        for j in range(cols):
            if(j >= 3-i and j <= 3+i):
                if j <= ((cols-1)//2):
                    # increament the character
                    char += 1
                else:
                    # decreament the character
                    char -= 1
                print(chr(char) , end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    rows = 4
    cols = 7
    printPattern(rows , cols)