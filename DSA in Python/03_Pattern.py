"""

*****
****
***
**
*

"""

def printPattern(rows , cols):
    for i in range(rows):
        for j in range(cols):
            if j <= (4-i):
                print("*" , end="")
        print()

if __name__ == "__main__":
    rows = 5
    cols = 5

    printPattern(rows,cols)
