"""

E
DE
CDE
BCDE
ABCDE

"""

def printPattern(rows , cols):
    for i in range(rows):
        char = ord('E') - i
        for j in range(cols):
            if j <= i:
                print(chr(char), end="")
                char += 1
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5
    printPattern(rows , cols)