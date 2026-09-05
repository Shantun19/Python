"""

A
BB
CCC
DDDD
EEEEE

"""

def printPattern(rows , cols):
    char = ord('A') - 1
    for i in range(rows):
        char += 1
        for j in range(cols):
            if j <= i:
                print(chr(char) , end="")
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5
    printPattern(rows , cols)