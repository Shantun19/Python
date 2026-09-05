"""
ABCDE
ABCD
ABC
AB
A

"""

def printPattern(rows , cols):
    for i in range(rows):
        char = ord('A')
        for j in range(cols):
            if(j <= 4-i):
                print(chr(char) , end="")
                char += 1
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5
    printPattern(rows , cols)